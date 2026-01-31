# Security Features Provided by Django

Django is designed with security in mind and provides many built-in features to help developers build secure web applications by default.

## Key Security Features

### 1. SQL Injection Protection
- Django ORM automatically escapes queries, preventing SQL injection attacks.

### 2. Cross-Site Scripting (XSS) Protection
- Django’s template system escapes variables by default, reducing XSS risks.

### 3. Cross-Site Request Forgery (CSRF) Protection
- Built-in CSRF middleware and template tags protect against CSRF attacks on forms.

### 4. Clickjacking Protection
- Django provides middleware to set the `X-Frame-Options` header, preventing clickjacking.

### 5. Secure Password Storage
- Passwords are hashed using strong algorithms (PBKDF2, Argon2, bcrypt, or SHA1).

### 6. HTTPS Support
- Django supports secure cookies and settings to enforce HTTPS (e.g., `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS`).

### 7. Session Security
- Sessions are stored securely and can be configured to use signed cookies.

### 8. User Authentication System
- Built-in authentication and permissions framework for managing users and access control.

### 9. Host Header Validation
- Prevents HTTP Host header attacks by validating allowed hosts (`ALLOWED_HOSTS` setting).

### 10. Other Protections
- Automatic escaping of output in templates
- Protection against directory traversal
- Option to sign cookies and data

## Best Practices
- Always keep Django and dependencies up to date.
- Use Django’s security settings in production.
- Regularly review the [Django security checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/).

## Resources
- [Django Security Documentation](https://docs.djangoproject.com/en/stable/topics/security/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)

---
Django’s built-in security features help you build robust and secure web applications with minimal effort.
