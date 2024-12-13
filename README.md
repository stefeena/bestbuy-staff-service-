# Best Buy Staff-Service Microservice

## Brief Explanation

The **Staff-Service** is a microservice developed to manage staff information for Best Buy's internal system. It provides CRUD (Create, Read, Update, Delete) operations for staff data via REST APIs. The service stores staff details such as ID, name, position, department, email, and phone number in memory, ensuring fast and scalable access to staff information. The service is built with the **12-factor app** principles to ensure scalability, maintainability, and ease of deployment in cloud-native environments.

## CRUD Operations Documentation

### 1. **Create Staff**
   - **Endpoint**: `POST /staff`
   - **Description**: Creates a new staff member.
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "position": "Manager",
       "department": "Sales",
       "email": "johndoe@bestbuy.com",
       "phone": "123-456-7890"
     }
     ```
   - **Response**: Returns the newly created staff member's data with a unique ID.
   
### 2. **Read Staff**
   - **Endpoint**: `GET /staff/{id}`
   - **Description**: Retrieves the details of a staff member by ID.
   - **Response**: Returns the staff member's data.
   - **Example**:
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "position": "Manager",
       "department": "Sales",
       "email": "johndoe@bestbuy.com",
       "phone": "123-456-7890"
     }
     ```

### 3. **Update Staff**
   - **Endpoint**: `PUT /staff/{id}`
   - **Description**: Updates the information of an existing staff member.
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "position": "Senior Manager",
       "department": "Sales",
       "email": "john.doe@bestbuy.com",
       "phone": "123-456-7891"
     }
     ```
   - **Response**: Returns the updated staff member's data.

### 4. **Delete Staff**
   - **Endpoint**: `DELETE /staff/{id}`
   - **Description**: Deletes a staff member by ID.
   - **Response**: Returns a success message confirming the staff member has been deleted.

## Task Breakdown

### Tasks Completed:

1. **Developed the Staff-Service Microservice**:
   - Implemented REST APIs for CRUD operations on staff information.
   - Stored data in memory, following the 12-factor principles.

2. **Containerized the Service**:
   - Created a Docker image for the service.
   - Pushed the Docker image to my personal Docker Hub account.

3. **Deployed the Service to Azure Kubernetes Service (AKS)**:
   - Set up an AKS cluster.
   - Created a Kubernetes deployment YAML file for staff-service and exposed it via a service.

4. **Set Up CI/CD Pipeline**:
   - Configured GitHub Actions to automate the build, test, and deployment process.

5. **Created and Updated README**:
   - Provided clear documentation for the service's functionality and usage.

## Technical Issues Encountered

1. **Issue with Docker Image Build**: Encountered an error during Docker image build due to missing dependencies in the `Dockerfile`. Fixed by ensuring that all necessary dependencies were included and properly configured.
   
2. **Kubernetes Deployment Failure**: The initial deployment in AKS failed due to an incorrect configuration in the YAML file. Resolved by fixing the image reference and ensuring proper namespace and environment settings.

3. **CI/CD Pipeline Errors**: The pipeline was not triggering correctly due to misconfigured secrets. This was resolved by correctly setting up environment variables and linking the repository to the appropriate Docker and Kubernetes services.

## External Links

- [Docker Hub Repository](https://hub.docker.com/repository/docker/stefeena/bestbuy-staff-service)
- [GitHub Repository](https://github.com/stefeena/bestbuy-staff-service)

---


