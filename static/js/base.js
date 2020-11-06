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
                console.log('create tag');
                // Don't offset to create a tag if there is no @ symbol
                if (params.term.indexOf('@') === -1) {
                    // Return null to disable tag creation
                    return null;
                }
                
                return {
                    id: params.term,
                    text: params.term
                }
            },
            tags: true,
        });
    });
  })