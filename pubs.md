---
layout: page
title: Publications
permalink: /pubs/
---

For the most up-to-date list of Shokat Lab publications, this page links to externally hosted publication records rather than locally hosted PDFs.

<p>
  <a href="https://profiles.ucsf.edu/kevan.shokat" target="_blank" rel="noopener">
    View Kevan Shokat's UCSF Profiles publication page
  </a>
</p>

<div id="profiles_publications">
  <p>Loading publications from UCSF Profiles...</p>
</div>

<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<script>
function add_profiles_publications(identifier_type, identifier) {
  $.getJSON(
    'https://api.profiles.ucsf.edu/json/v2/?source=shokatlab.ucsf.edu&' +
      identifier_type + '=' + identifier + '&publications=full&callback=?',
    function(response) {
      if (!response || response.error || !response.Profiles || !response.Profiles[0]) {
        $('#profiles_publications').html(
          '<p>Publications could not be loaded. Please visit <a href="https://profiles.ucsf.edu/kevan.shokat">Kevan Shokat\\'s UCSF Profiles page</a>.</p>'
        );
        return;
      }

      var data = response.Profiles[0];

      if (data.Publications && data.Publications.length > 0) {
        $('#profiles_publications').empty();
        $('#profiles_publications').append('<ol id="profiles_publications_list"></ol>');

        jQuery.each(data.Publications, function() {
          var li = $('<li class="profiles_publications_li" />');

          if (this.PublicationTitle) {
            li.append(document.createTextNode(this.PublicationTitle + ' '));
          }

          if (this.PublicationSource && this.PublicationSource.length > 0) {
            var source = this.PublicationSource[0];
            if (source.PublicationSourceURL && source.PublicationSourceName) {
              li.append(
                $('<a class="profiles_publication_link" />')
                  .attr('href', source.PublicationSourceURL)
                  .attr('target', '_blank')
                  .attr('rel', 'noopener')
                  .text('View on ' + source.PublicationSourceName)
              );
            }
          }

          $('#profiles_publications_list').append(li);
        });
      } else {
        $('#profiles_publications').html(
          '<p>No publications were returned. Please visit <a href="https://profiles.ucsf.edu/kevan.shokat">Kevan Shokat\\'s UCSF Profiles page</a>.</p>'
        );
      }
    }
  );
}

add_profiles_publications('ProfilesURLName', 'kevan.shokat');
</script>