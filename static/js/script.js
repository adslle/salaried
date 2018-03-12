$(document).ready(function () {

    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 30, // Creates a dropdown of 15 years to control year
        format: 'yyyy-mm-dd' //%Y-%m-%d
    });
    file_input = $('.file-input');
    file_input.wrap('<div class = "file-field input-field"><div class = "btn"></div></div>');
    $("<span>Browse</span>").insertBefore(file_input);
    $("<div class = \"file-path-wrapper\">\n" +
        "                     <input class = \"file-path validate\" type = \"text\"\n" +
        "                        placeholder = \"Upload file\" />\n" +
        "                  </div>").insertAfter(file_input.parent());
    $("[for=id_form-0-attached_piece]").remove()
    $("[for=id_attached_piece]").remove()

    $(document).on('DOMNodeInserted', function (e) {
        if ($(e.target).hasClass('link-formset')) {
            //console.log($(e.target)[0])
            $($(e.target)[0]).find('div > p:nth-child(3)').contents().filter(function () {
                return this.nodeType === 3 || this.localName === 'a';
            }).remove();
            $($(e.target)[0]).find('div.error-form').remove();

        }
    });


    $('select').removeAttr('required')
})

$(document).on('ready', function () {
    $('.link-formset').formset({
        addText: 'Add Attached piece',
        deleteText: 'Remove Attached piece'
    });
});
