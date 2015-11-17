# slapp
Service Level Agreement APP

# Service Provider Review App

## User Roles
* Company-> Makes the contract with both: Provider and Client
* Provider - > Subject of Review: Has to provide the service in an accurate way.
- You woudl have a company profile.
* Client -> Expects a Service Level Agreement to be delivered.
- Provider gives a ticket: SLA.com/!"·!"$!"$"·%"% unique.

## Workflows
* Company creates its own profile
* Company creates SLA

## Models

* Company Profile:
    - Company name
    - Employee/Providers [ ]

* SLA:
    - ID
    - CLIENT
    - PROVIDER
    - TERMS OF CONTRACT [
        - Delivered in Time: BOOLEAN
        - Delivered in QUality: BOOLEAN
        - Was the person Polite: BOOLEAN
        - Was the work Clean: BOOLEAN
        ]

## Models
* Company
    - Company name
    - Employee/Providers [ ]
    
* Provider
  - ID
  - Picture

* SLA:
    - ID
    - Reference to the Client
    - Reference to the Provider
    - Expected Delivery Time (DateField)

## Workflows

- Company can signup
- Company can signin
- Company can create Provider profiles
- Company can modify/delete Provider profiles
- Company can create SLAs
- Company can look at its own SLAs (in a list)
- Company can modify/delete SLAs