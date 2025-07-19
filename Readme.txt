Little Lemon Restaurant API Documentation

API Endpoints:

1. Authentication
   - User Registration: POST /auth/users/
   - Token Generation: POST /auth/token/login/
   - Token Deletion: POST /auth/token/logout/

2. Booking API
   - List/Create Bookings: GET, POST /api/bookings/
   - Retrieve/Update/Delete Booking: GET, PUT, PATCH, DELETE /api/bookings/{id}/

3. Menu API
   - List/Create Menu Items: GET, POST /api/menu/
   - Retrieve/Update/Delete Menu Item: GET, PUT, PATCH, DELETE /api/menu/{id}/

Testing Instructions:
1. Create a user via /auth/users/
2. Obtain an authentication token via /auth/token/login/
3. Use the token in the Authorization header for all API requests (Token {your_token})
4. Test endpoints using Insomnia or similar REST client

