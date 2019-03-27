"use strict";
$(document).ready(function() {
  $.when(
    $.getScript("/js/fuse.min.js"),
    $.getScript("/js/masterArr.js"),
    $.Deferred(function(deferred) {
      $(deferred.resolve);
    })
    ).done(function() {
      console.log("total entries in master list: " + masterList.length);
      $("#resultList").append("<span class='num-entries'><b>"+ masterList.length+"</b> Entries indexed</span>");

      var fuseOptions = {
        shouldSort: true,
        threshold: 0.6,
        location: 0,
        distance: 100,
        maxPatternLength: 32,
        minMatchCharLength: 1,
        keys: ["name","shortform"]
      };
      var fuse = new Fuse(masterList, fuseOptions);

      function query() {
        var queryTerms = document.getElementById("searchBar").value;
        $.get("?log=" + queryTerms);
        var result = fuse.search(queryTerms);
        var resultListHTML = "";
        for (var i = 0; i < Math.min(10, result.length); i++) {
          if ('url' in result[i]) {
            resultListHTML +=
            '<li><a href="' +
            result[i].url +
            '" target="_blank">' +
            result[i].name +
            '</a></li>';
          } else {
            resultListHTML +=
            '<li><a>' +
            result[i].name +
            '</a></li>';
          }
        }
        $("#resultList").empty();
        $("#resultList").append(resultListHTML);
      }
      document
      .getElementById("searchBar")
      .addEventListener("keyup", function(event) {
        event.preventDefault();
          query();
      });
  }); //end of main function
  });
