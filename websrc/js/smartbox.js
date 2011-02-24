/*
 *  Pyaste SmartBox - Input interpretor
 */

var smartbox = (function()
{
    var $ = window.jQuery,
    s={},
    commentStyle = {"python": {oneline: "#",multiline: '"""'}},
    lang = null;
    
    
    function parseContent(e)
    {
	if(lang === null)
	    {
		$.each(commentStyle,function(clang,v)
		       {
			   var L = new RegExp("^"+v.multiline+"\s* \*pyaste\* [\n.]*"+v.multiline+"$",m).test(e.val());
			   if(L)
			       {
				   lang = clang;
				   return false;
			       }
		       });
	    }
    }

    function newInput(ev)
    {
	parseContent($(this));
    }

    s.attach = function(elem)
    {
	elem.key
    }

    return s;
})();