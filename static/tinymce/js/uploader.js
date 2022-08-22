tinymce.init({
  height: 560,
  width: 1000,
  cleanup_on_startup: true,
  custom_undo_redo_levels: 20,
  theme: 'silver',
  selector: 'textarea',  // change this value according to your HTML
  plugins: 'image textcolor save link image media preview codesample contextmenu table code advlist lists fullscreen insertdatetime nonbreaking directionality searchreplace wordcount visualblocks visualchars autolink charmap print hr anchor pagebreak paste  help spellchecker',
  menubar: true,
  toolbar1: 'fullscreen preview bold italic underline | fontselect fontsizeselect | forecolor backcolor | alignleft alignright | aligncenter alignjustify | indent outdent | bullist numlist table | link image media | codesample | removeformat casechange checklist | superscript subscript | export table  help',
  toolbar2: 'visualblocks visualchars | charmap hr pagebreak nonbreaking anchor | code |',
  fontsize_formats: "8pt 9pt 10pt 11pt 12pt 13pt 14pt 15pt 16pt 17pt 18pt 19pt 20pt 21pt 22pt 23pt 24pt 30pt 36pt 48pt 60pt 72pt 96pt",
    /* enable title field in the Image dialog*/
  image_title: true,
  tinycomments_mode: 'embedded',
    /* enable automatic uploads of images represented by blob or data URIs*/
  automatic_uploads: true,
    /*
      URL of our upload handler (for more details check: https://www.tiny.cloud/docs/configure/file-image-upload/#images_upload_url)
      images_upload_url: 'postAcceptor.php',
      here we add custom filepicker only to Image dialog
    */
  advlist_bullet_styles: "squre",
  advlist_number_styles: "decimal",
  file_picker_types: 'image',
    /* and here's our custom image picker*/
    file_picker_callback: function (cb, value, meta) {
      var input = document.createElement('input');
      input.setAttribute('type', 'file');
      input.setAttribute('accept', 'image/*');
  
      /*
        Note: In modern browsers input[type="file"] is functional without
        even adding it to the DOM, but that might not be the case in some older
        or quirky browsers like IE, so you might want to add it to the DOM
        just in case, and visually hide it. And do not forget do remove it
        once you do not need it anymore.
      */
  
      input.onchange = function () {
        var file = this.files[0];
  
        var reader = new FileReader();
        reader.onload = function () {
          /*
            Note: Now we need to register the blob in TinyMCEs image blob
            registry. In the next release this part hopefully won't be
            necessary, as we are looking to handle it internally.
          */
          var id = 'blobid' + (new Date()).getTime();
          var blobCache =  tinymce.activeEditor.editorUpload.blobCache;
          var base64 = reader.result.split(',')[1];
          var blobInfo = blobCache.create(id, file, base64);
          blobCache.add(blobInfo);
  
          /* call the callback and populate the Title field with the file name */
          cb(blobInfo.blobUri(), { title: file.name });
        };
        reader.readAsDataURL(file);
      };
  
      input.click();
    },
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
  });