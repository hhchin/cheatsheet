'use strict';
$(document).ready(function(){
  $.when(
    $.getScript( "/js/fuse.min.js" ),
    $.getScript( "/js/fuseIODemoArr.js"),
    $.Deferred(function( deferred ){
      $( deferred.resolve );
    })
    ).done(function(){
      console.log('done');
      console.log(masterList);

      var fuseOptions = {
        shouldSort: true,
        threshold: 0.6,
        location: 0,
        distance: 100,
        maxPatternLength: 32,
        minMatchCharLength: 1,
        keys: [
        "title",
        "author.firstName"
        ]
      };
      var fuse = new Fuse(masterList, fuseOptions); 
      
      function query() {
        var queryTerms = document.getElementById('searchBar').value;
        var result = fuse.search(queryTerms);
        console.log(result);
        var resultListHTML = '';
        var link = "https://www.google.com";
        for(var i=0; i<result.length; i++){
          resultListHTML +="<li><a href=\""+link+"\" target=\"_blank\">"+result[i].title+"</a></li>";
        }
        $("#resultList").empty();
        $("#resultList").append(resultListHTML);
      }

      document.getElementById('searchSubmit').addEventListener('click', query);
      document.getElementById('searchBar').addEventListener('keyup', function(event) {
        event.preventDefault();
        if (event.keyCode === 13) {
          query();
        }
      });

    }); //end of main function
  });
