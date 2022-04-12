let editor;

window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/fortran");
}



function executeCode() {

    $.ajax({

        url: "/output",

        method: "POST",
        data: JSON.stringify({
            language: $("#languages").val(),
            code: editor.getSession().getValue()
        } ),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        
        success: function(response) {
            $(".output").text(response.output)
        }
    })
} 