from django.shortcuts import render
from decimal import Decimal

def ecommerce_view(request):
    context = {
        'store_name': 'Tech Gadget Store',
        'products': [
            {
                'id': 1,
                'name': 'Wireless Bluetooth Headphones',
                'slug': 'wireless-bluetooth-headphones',
                'description': 'Premium wireless headphones with noise cancellation and 30-hour battery life.',
                'price': Decimal('129.99'),
                'original_price': Decimal('159.99'),
                'discount': 19,
                'in_stock': True,
                'stock_quantity': 45,
                'category': 'Audio',
                'rating': 4.5,
                'reviews_count': 128,
                'features': ['Noise Cancellation', '30h Battery', 'Bluetooth 5.0', 'Comfort Fit'],
                'images': ['headphones_1.jpg', 'headphones_2.jpg'],
                'created_at': '2024-01-15',
                'is_featured': True
            },
            {
                'id': 2,
                'name': 'Smart Fitness Watch',
                'slug': 'smart-fitness-watch',
                'description': 'Advanced fitness tracker with heart rate monitoring, GPS, and waterproof design.',
                'price': Decimal('199.99'),
                'original_price': Decimal('249.99'),
                'discount': 20,
                'in_stock': True,
                'stock_quantity': 23,
                'category': 'Wearables',
                'rating': 4.3,
                'reviews_count': 89,
                'features': ['Heart Rate Monitor', 'GPS', 'Waterproof', 'Sleep Tracking'],
                'images': ['watch_1.jpg', 'watch_2.jpg'],
                'created_at': '2024-02-10',
                'is_featured': True
            },
            {
                'id': 3,
                'name': 'USB-C Charging Cable',
                'slug': 'usb-c-charging-cable',
                'description': 'High-speed USB-C charging cable with durable braided design.',
                'price': Decimal('19.99'),
                'original_price': Decimal('24.99'),
                'discount': 20,
                'in_stock': False,
                'stock_quantity': 0,
                'category': 'Accessories',
                'rating': 4.1,
                'reviews_count': 56,
                'features': ['3m Length', 'Fast Charging', 'Braided Cable', 'Durable'],
                'images': ['cable_1.jpg'],
                'created_at': '2024-03-01',
                'is_featured': False
            },
            {
                'id': 4,
                'name': 'Wireless Charging Pad',
                'slug': 'wireless-charging-pad',
                'description': '15W fast wireless charging pad compatible with all Qi-enabled devices.',
                'price': Decimal('49.99'),
                'original_price': Decimal('69.99'),
                'discount': 29,
                'in_stock': True,
                'stock_quantity': 12,
                'category': 'Accessories',
                'rating': 4.7,
                'reviews_count': 203,
                'features': ['15W Fast Charge', 'Qi Compatible', 'LED Indicator', 'Non-slip Base'],
                'images': ['charger_1.jpg', 'charger_2.jpg'],
                'created_at': '2024-01-28',
                'is_featured': True
            }
        ],
        'categories': [
            {'name': 'Audio', 'product_count': 1},
            {'name': 'Wearables', 'product_count': 1},
            {'name': 'Accessories', 'product_count': 2},
            {'name': 'Computers', 'product_count': 0}
        ],
        'cart_items_count': 3,
        'total_cart_value': Decimal('289.97'),
        'featured_products_count': 3,
        'on_sale_products': 4
    }
    return render(request, 'ecommerce/index.html', context)