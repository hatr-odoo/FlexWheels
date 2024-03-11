from datetime import datetime
from odoo import http

class flexwheelsController(http.Controller):

    @http.route(['/cars', '/cars/page/<int:page>'] , auth='public', website=True)
    def index(self, page='1', filter_date=None, **kw):
        Car = http.request.env['flexwheels.car']
        domain = [('is_available', '=', 'True')]
        order = 'create_date DESC'
        
        # Convert the 'listed_after' parameter to a datetime object if provided
        if filter_date:
            filter_date = datetime.strptime(filter_date, '%Y-%m-%d').date()
            domain.append(('create_date', '>=', filter_date))
            
        # Number of items per page
        items_per_page = 6
 
        # Calculate the total number of pages
        total_cars = Car.search_count(domain)
        # total_pages = (total_properties - 1) // items_per_page + 1
        
        # Pager
        pager = http.request.website.pager(
            url="/cars", 
            total=total_cars, 
            page=int(page), 
            step=items_per_page,
            url_args={'filter_date': filter_date}
        )
                # Load data as per pager
        cars = http.request.env['flexwheels.car'].search(domain, order=order, limit=items_per_page, offset=pager['offset'])
        
        return http.request.render('flexwheels.flexwheels_car_list', {
            'cars': cars,
            'pager': pager
        })
        
    @http.route('/cars/<int:id>', auth='public', website=True)
    def property_index(self, id, **kw):
        return http.request.render('flexwheels.car_index', {
            'car': http.request.env['flexwheels.car'].browse(id)
        })
