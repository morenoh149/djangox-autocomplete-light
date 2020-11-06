/**
 * if a company does not exist in the database,
 * accept user input as a ticker request for backend to fetch from
 * data provider
 */
document.addEventListener('dal-init-function', function () {
    yl.registerFunction('ticker_autocomplete_init', function ($, element) {
        console.log('baz');
        
        var $element = $(element);
        $element.select2({
            placeholder: 'Company',
            ajax: {
                url: "/company-autocomplete",
                delay: 250,
            },
            createTag: function(params) {
                console.log('createTag', params);
                return {
                    id: params.term,
                    text: params.term.toUpperCase(),
                    isTag: true
                }
            },
            tags: true,
            // insertTag: function(data, tag) {
            //     tag.text = "Add: " + tag.text;
            //     // tag.isTag = true;
            //     data.push(tag);
            // },
            // language: { 
            //     noResults: function (event) {
            //       var term = event.target.value;
            //       return '<a href="#">add item ' + term + '</a>' 
            //     },
            //     escapeMarkup: function (markup) {
            //           return markup;
            //     }
            //   }
        });
        $element.on("change:selecting", function(e) {
            console.log('select');
            if (e.params && e.params.data) {

                var data = e.params.data;
                var requestForm = document.querySelector('#form-ticker-request');
                if (data.isTag) {
                    console.log('local tag selected', data);
                    requestForm.classList.remove('d-none');
                } else {
                    requestForm.classList.add('d-none');
                }
            }
        });
    });
  })