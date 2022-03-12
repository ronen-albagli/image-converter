### APP ###

This is your app folder, it contains your actual application with all its business logic

folder info:

api: 

Create them independently by APIRouter, instead of gathering all your APIs inside one file.

schemas:

Schemas are your Pydantic models, we call it schemas because it is actually used for creating OpenAPI schemas since FastAPI is based on OpenAPI specification we use schemas everywhere, from Swagger generation to endpoint's expected request body.

Models:

It is for your database models