tinymce.init({
    selector: '#bio',
    plugins: 'lists link',
    toolbar: 'undo redo | bold italic | alignleft aligncenter alignright | bullist numlist | link',
    menubar: false,
    setup: function(editor) {
        editor.on('change', function() {
            var content = editor.getContent();
            $('#hidden_bio').val(content);
        });
    }
});

tinymce.init({
    selector: '#experience',
    plugins: 'lists link',
    toolbar: 'undo redo | bold italic | alignleft aligncenter alignright | bullist numlist | link',
    menubar: false,
    setup: function(editor) {
        editor.on('change', function() {
            var content = editor.getContent();
            $('#hidden_experience').val(content);
        });
    }
});

tinymce.init({
    selector: '#education',
    plugins: 'lists link',
    toolbar: 'undo redo | bold italic | alignleft aligncenter alignright | bullist numlist | link',
    menubar: false,
    setup: function(editor) {
        editor.on('change', function() {
            var content = editor.getContent();
            $('#hidden_education').val(content);
        });
    }
});

tinymce.init({
    selector: '#skills',
    plugins: 'lists link',
    toolbar: 'undo redo | bold italic | alignleft aligncenter alignright | bullist numlist | link',
    menubar: false,
    setup: function(editor) {
        editor.on('change', function() {
            var content = editor.getContent();
            $('#hidden_skills').val(content);
        });
    }
});

tinymce.init({
    selector: '#contacts',
    plugins: 'lists link',
    toolbar: 'undo redo | bold italic | alignleft aligncenter alignright | bullist numlist | link',
    menubar: false,
    setup: function(editor) {
        editor.on('change', function() {
            var content = editor.getContent();
            $('#hidden_contacts').val(content);
        });
    }
});
