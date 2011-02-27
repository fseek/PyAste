<%inherit file="base.tpl"/>
<%def name="title()">Viewing Paste</%def>
<%def name="script()">
<script>
  var editor;
  head.js("/js/libs/ace/src/ace.js","/js/libs/ace/src/theme-twilight.js",function(){
    $(function(){
      editor=ace.edit("view-paste");
      editor.setTheme("ace/theme/twilight");
      head.js("/js/libs/ace/src/mode-${lang}.js",function(){
        var m = require("/ace/mode/${lang}").Mode;
        editor.getSession().setMode(new m());
      });
    });
  });
</script>
</%def>
<div id="view-paste">
  ${code | h}
</div>
