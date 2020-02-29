# DAM-ProjectCore

## Description
Docker architecture to deploy a MySQL database and an API rest implemented in Falcon (Python framework).

## Legend
- [A] Indicates that requires Authorization header (token)

## Resources

### Account Resources
- POST /account/create_token
- [A] POST /account/delete_token
- [A] GET /account/profile

### Users Resources
- POST /users/register
- [A] GET /users/show/{username:str}

