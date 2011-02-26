<!doctype html>  
<!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ --> 
<!--[if lt IE 7 ]> <html class="no-js ie6"> <![endif]--> 
<!--[if IE 7 ]>    <html class="no-js ie7"> <![endif]--> 
<!--[if IE 8 ]>    <html class="no-js ie8"> <![endif]--> 
<!--[if (gte IE 9)|!(IE)]><! -->
<html class="no-js">
  <!--<![endif]--> 
  <title>${self.title()}</title>
  <link rel="stylesheet" href="/css/1140.css?v=1"></link>
  <link rel="stylehseet" href="/css/style.css?v=2"></link>
  <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
  <link href='http://fonts.googleapis.com/css?family=Kreon' rel='stylesheet' type='text/css'>
  <script src="//ajax.cdnjs.com/ajax/libs/headjs/0.9/head.min.js"></script>
  <body>
    <div id="container" class="container">
      <header class="row" id="header-main">
	<div class="onecol"><img src="/images/edit-paste.svg" width=42 height=42 /></div>
	<div class="ninecol last">
	  <h3>Pyaste - Python Pastebin</h3>
	</div>
      </header>
      ${self.body()}
      <footer id="main-footer" class="row">
	${self.footer()}
      </footer>
    </div>
    <script src="//ajax.googleapis.com/ajax/jquery/1.5.0/jquery.js"></script>
    <script>!window.jQuery && document.write(unescape('%3Cscript src="js/libs/jquery-1.5.0.js"%3E%3C/script%3E'))</script>
    <script src="/js/plugins.js"></script>
    <script src="/js/script.js"></script>
    <!--[if lt IE 7]>
	<script src="/js/libs/dd_belatedpng.js"></script>
	<script>DD_belatedPNG.fix('img, .png_bg');</script>
    <![endif]-->
    ${self.script}
  </body>
</html>
<%def name="footer()">
<p>&copy Skyoix 2010. Individual pastes are owned by the poster</p>
</%def>
