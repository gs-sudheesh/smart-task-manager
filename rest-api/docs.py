"""
OpenAPI Documentation Module
============================

This module provides endpoints to serve the OpenAPI specification and
Swagger UI for the Task Manager REST API documentation.

Features:
    - Serves OpenAPI YAML specification
    - Provides Swagger UI interface
    - API documentation accessibility
    - Interactive API testing

Usage Scenarios:
    - API documentation for developers
    - Interactive API testing interface
    - API specification sharing
    - Client SDK generation

Author: Smart Task Manager Team
Version: 1.0.0
"""

import os
import yaml
from flask import render_template_string, jsonify, request
from config.app_config import app

# Swagger UI HTML template
SWAGGER_UI_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Manager API Documentation</title>
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui.css" />
    <style>
        html {
            box-sizing: border-box;
            overflow: -moz-scrollbars-vertical;
            overflow-y: scroll;
        }
        *, *:before, *:after {
            box-sizing: inherit;
        }
        body {
            margin:0;
            background: #fafafa;
        }
        .swagger-ui .topbar {
            background-color: #2c3e50;
        }
        .swagger-ui .topbar .download-url-wrapper .select-label {
            color: #fff;
        }
    </style>
</head>
<body>
    <div id="swagger-ui"></div>
    <script src="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-bundle.js"></script>
    <script src="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-standalone-preset.js"></script>
    <script>
        window.onload = function() {
            const ui = SwaggerUIBundle({
                url: '/api/docs/openapi.yaml',
                dom_id: '#swagger-ui',
                deepLinking: true,
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIStandalonePreset
                ],
                plugins: [
                    SwaggerUIBundle.plugins.DownloadUrl
                ],
                layout: "StandaloneLayout",
                tryItOutEnabled: true,
                requestInterceptor: function(request) {
                    // Add session cookie to requests if available
                    const cookies = document.cookie.split(';');
                    for (let cookie of cookies) {
                        const [name, value] = cookie.trim().split('=');
                        if (name === 'session') {
                            request.headers['Cookie'] = `session=${value}`;
                            break;
                        }
                    }
                    return request;
                }
            });
        };
    </script>
</body>
</html>
'''

@app.route('/api/docs')
def swagger_ui():
    """
    Serve Swagger UI interface for API documentation.
    
    This endpoint provides an interactive web interface for exploring
    and testing the Task Manager REST API. It includes the complete
    OpenAPI specification with interactive forms for testing endpoints.
    
    Returns:
        HTML: Swagger UI interface with embedded OpenAPI specification
    
    Usage Scenarios:
        - API documentation browsing
        - Interactive endpoint testing
        - API specification exploration
        - Developer onboarding
    
    Features:
        - Interactive API testing
        - Request/response examples
        - Authentication support
        - Schema documentation
    """
    return render_template_string(SWAGGER_UI_TEMPLATE)

@app.route('/api/docs/openapi.yaml')
def openapi_spec():
    """
    Serve the OpenAPI specification in YAML format.
    
    This endpoint returns the complete OpenAPI 3.0 specification
    for the Task Manager REST API in YAML format. It can be used
    by Swagger UI, code generators, and other API documentation tools.
    
    Returns:
        YAML: OpenAPI 3.0 specification document
    
    Usage Scenarios:
        - Swagger UI integration
        - API client generation
        - API specification sharing
        - Documentation tool integration
    
    Content-Type:
        - application/x-yaml
        - text/yaml
    """
    try:
        # Get the directory of this file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        openapi_file = os.path.join(current_dir, 'openapi.yaml')
        
        with open(openapi_file, 'r', encoding='utf-8') as file:
            yaml_content = file.read()
        
        return yaml_content, 200, {'Content-Type': 'application/x-yaml'}
    except FileNotFoundError:
        return jsonify({"error": "OpenAPI specification not found"}), 404
    except Exception as e:
        return jsonify({"error": f"Error loading specification: {str(e)}"}), 500

@app.route('/api/docs/openapi.json')
def openapi_spec_json():
    """
    Serve the OpenAPI specification in JSON format.
    
    This endpoint returns the complete OpenAPI 3.0 specification
    for the Task Manager REST API in JSON format. It's useful for
    tools that prefer JSON over YAML format.
    
    Returns:
        JSON: OpenAPI 3.0 specification document
    
    Usage Scenarios:
        - JSON-based API tools
        - Programmatic specification processing
        - API client generation
        - Integration with JSON-based documentation tools
    """
    try:
        # Get the directory of this file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        openapi_file = os.path.join(current_dir, 'openapi.yaml')
        
        with open(openapi_file, 'r', encoding='utf-8') as file:
            yaml_content = yaml.safe_load(file)
        
        return jsonify(yaml_content)
    except FileNotFoundError:
        return jsonify({"error": "OpenAPI specification not found"}), 404
    except yaml.YAMLError as e:
        return jsonify({"error": f"Error parsing YAML: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Error loading specification: {str(e)}"}), 500

@app.route('/api/docs/health')
def docs_health():
    """
    Health check endpoint for documentation service.
    
    This endpoint provides a simple health check for the documentation
    service, indicating whether the OpenAPI specification is available
    and the documentation service is functioning properly.
    
    Returns:
        JSON: Health status information
    
    Usage Scenarios:
        - Service monitoring
        - Health checks
        - Documentation service validation
    """
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        openapi_file = os.path.join(current_dir, 'openapi.yaml')
        
        if os.path.exists(openapi_file):
            return jsonify({
                "status": "healthy",
                "service": "Task Manager API Documentation",
                "openapi_spec_available": True,
                "endpoints": {
                    "swagger_ui": "/api/docs",
                    "openapi_yaml": "/api/docs/openapi.yaml",
                    "openapi_json": "/api/docs/openapi.json"
                }
            })
        else:
            return jsonify({
                "status": "unhealthy",
                "service": "Task Manager API Documentation",
                "openapi_spec_available": False,
                "error": "OpenAPI specification file not found"
            }), 503
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "service": "Task Manager API Documentation",
            "error": str(e)
        }), 500
