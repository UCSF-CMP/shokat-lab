---
layout: page
title: Publications
permalink: /pubs/
---

<p>
  For the most up-to-date list of Shokat Lab publications, this page links to externally hosted publication records rather than locally hosted PDFs.
</p>

<p>
  <a href="https://profiles.ucsf.edu/kevan.shokat" target="_blank" rel="noopener">
    View Kevan Shokat's UCSF Profiles publication page
  </a>
</p>

<div id="profiles_publications">
  <p id="profiles_publications_loading">Loading publications from UCSF Profiles...</p>
</div>

<p>
  Publication data provided by
  <a href="https://profiles.ucsf.edu/" target="_blank" rel="noopener">
    UCSF Profiles
  </a>, powered by UCSF CTSI.
</p>

<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<script>
// Same UCSF Profiles JSON API pattern used by kevan.md
add_profiles_publications('ProfilesURLName', 'kevan.shokat');

function add_profiles_publications(identifier_type, identifier) {
  var request_completed = false;

  $.getJSON(
    'https://api.profiles.ucsf.edu/json/v2/?source=anatomy.ucsf.edu&' +
      identifier_type + '=' + identifier + '&publications=full&callback=?',
    function(response) {
      request_completed = true;

      if (!response || response.error || !response.Profiles || response.Profiles.length === 0) {
        show_publications_fallback();
        return;
      }

      $(document).ready(function() {
        var data = response.Profiles[0];

        if (data.Publications && data.Publications.length > 0) {
          render_publications(data.Publications);
        } else {
          show_publications_fallback();
        }
      });
    }
  );

  // JSONP failures do not always trigger .fail(), so use a manual timeout.
  setTimeout(function() {
    if (!request_completed) {
      show_publications_fallback();
    }
  }, 8000);
}

function render_publications(publications) {
  $('#profiles_publications').empty();

  var list = $('<ol id="profiles_publications_list"></ol>');

  jQuery.each(publications, function() {
    var li = $('<li class="profiles_publications_li"></li>');

    if (this.PublicationTitle) {
      li.append(document.createTextNode(this.PublicationTitle + ' '));
    } else {
      li.append(document.createTextNode('Publication record '));
    }

    if (this.PublicationSource && this.PublicationSource.length > 0) {
      var source = get_best_non_pdf_source(this.PublicationSource);

      if (source && source.PublicationSourceURL) {
        li.append(
          $('<a class="profiles_publication_link"></a>')
            .attr('href', source.PublicationSourceURL)
            .attr('target', '_blank')
            .attr('rel', 'noopener')
            .text('View on ' + source.PublicationSourceName)
        );
      } else {
        li.append(
          $('<a class="profiles_publication_link"></a>')
            .attr('href', 'https://profiles.ucsf.edu/kevan.shokat')
            .attr('target', '_blank')
            .attr('rel', 'noopener')
            .text('View on UCSF Profiles')
        );
      }
    } else {
      li.append(
        $('<a class="profiles_publication_link"></a>')
          .attr('href', 'https://profiles.ucsf.edu/kevan.shokat')
          .attr('target', '_blank')
          .attr('rel', 'noopener')
          .text('View on UCSF Profiles')
      );
    }

    list.append(li);
  });

  $('#profiles_publications').append(list);
}

function get_best_non_pdf_source(publication_sources) {
  for (var i = 0; i < publication_sources.length; i++) {
    var source = publication_sources[i];
    var url = source.PublicationSourceURL || '';

    if (url && url.toLowerCase().indexOf('.pdf') === -1) {
      return source;
    }
  }

  return null;
}

function show_publications_fallback() {
  $('#profiles_publications')
    .empty()
    .show()
    .append(
      '<p>Publications could not be loaded automatically. Please visit ' +
      '<a href="https://profiles.ucsf.edu/kevan.shokat" target="_blank" rel="noopener">' +
      'Kevan Shokat\\'s UCSF Profiles publication page</a>.</p>'
    );
}
</script>