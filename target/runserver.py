#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app
from flask_cors import CORS

if __name__ == '__main__':
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    port = int(os.environ.get("PORT", 8081))
    app.run('0.0.0.0', port=port)

