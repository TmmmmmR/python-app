# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request, render_template_string

@app.errorhandler(404)
def page_not_found(e):
    template = """
<!DOCTYPE html>
<html lang="en">
<head>
            
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Page not found error!</title>

    <!-- Bootstrap Core CSS -->
    <link href="static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Morris Charts CSS -->
    <link href="static/css/morris.css" rel="stylesheet">
    
    <!-- Custom Fonts -->
    <link href="static/css/font-awesome.min.css" rel="stylesheet" type="text/css">
        
    <!-- Custom CSS -->
    <link href="static/css/startmin.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>
<body>

<div id="wrapper">
    <!-- Navigation -->

        <nav class="navbar navbar-inverse navbar-fixed-top" style="background-color:#00C8A1" role="navigation">
        
        <div class="navbar-header">
            <a class="navbar-brand" href="#" style="color:white;">Xebia hacking assessment</a>
        </div>

        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </button>

      
        <!-- Sidebar -->
        <div class="navbar-default sidebar" role="navigation">
            <div class="sidebar-nav navbar-collapse">
            </div>
        </div>
        
    </nav>
    <!-- Page Content -->
    <div id="page-wrapper">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-12">
                
                </div>
            </div>

            <h1 class="page-header">Page not found!</h1>
             <pre> the page you where looking for at <b>{0}</b>, was not found! </pre>
            </p>Please follow this link to return to <a href="/dashboard/1" style="color:blue;">home</a>
        </div>
    </div>
</div>

<!-- jQuery -->
<script src="static/js/jquery.min.js"></script>

<!-- Bootstrap Core JavaScript -->
<script src="static/js/bootstrap.min.js"></script>

<!-- Metis Menu Plugin JavaScript -->
<script src="static/js/metisMenu.min.js"></script>

<!-- Custom Theme JavaScript -->
<script src="static/js/startmin.js"></script>
</body>
</html>
    """.format(request.url)
    return render_template_string(template), 404
