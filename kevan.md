---
layout: faculty
title: Kevan Shokat
permalink: /kevan/
---

<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<script>
// we're grabbing data from the UCSF Profiles JSON API v2
// details at http://opendata.profiles.ucsf.edu/json-v2.html

// USER CONTENT HERE
add_profiles_user_content('ProfilesURLName', 'kevan.shokat');

// PROFILES SCRIPT FUNCTIONS
function add_profiles_user_content(identifier_type, identifier) {
  $.getJSON(
    'https://api.profiles.ucsf.edu/json/v2/?source=anatomy.ucsf.edu&' +
      identifier_type + '=' + identifier + '&publications=full&callback=?',
    function(response) {
      if (response) {
        if (response.error) {
          if (window.console && window.console.log) {
            console.log('Error from UCSF Profiles API: ' + response.error);
          }
        } else {
          $(document).ready(function() {
            var data = response.Profiles[0];

            if (data.Name) {
              $('#profiles_name').text(data.Name);
            }

            if (data.ProfilesURL) {
              $('#profiles_page_link_container')
                .empty()
                .show()
                .append('<a href="' + data.ProfilesURL + '" title="Go to UCSF Profiles, powered by CTSI" rel="me">UCSF Profiles page</a>');
            } else {
              $('#profiles_page_link_container').empty().hide();
            }

            if (data.PhotoURL) {
              $('#profiles_photo_container')
                .empty()
                .show()
                .append(
                  $('<img class="img-circle" id="profiles_photo" />')
                    .attr('src', data.PhotoURL)
                    .error(function() { this.style.display = 'none'; })
                );
            } else {
              $('#profiles_photo_container').empty().hide();
            }

            if (data.Narrative) {
              var truncated_narrative = data.Narrative
                .substr(0, 500)
                .replace(/[\s\r\n]/g, " ")
                .replace(/^(.+\.[\s\n\r]).*?$/g, "$1");
              $('#profiles_narrative').show().text(truncated_narrative);
            } else {
              $('#profiles_narrative').hide();
            }

            if (data.Email) {
              $('#profiles_email_link_container')
                .empty()
                .show()
                .append('<a href="mailto:' + data.Email + '">' + data.Email + '</a>');
            } else {
              $('#profiles_email_link_container').empty().hide();
            }

            if (data.Email || data.ProfilesURL) {
              $('#profiles_connect').show();
            } else {
              $('#profiles_connect').hide();
            }

            if (data.Publications && data.Publications.length > 0) {
              $('#profiles_publications ol').remove();
              $('#profiles_publications')
                .show()
                .append($('<ol id="profiles_publications_list"></ol>'));

              jQuery.each(data.Publications, function() {
                var li = $('<li class="profiles_publications_li" />');
                li.append(this.PublicationTitle + ' ');

                if (this.PublicationSource && this.PublicationSource.length > 0) {
                  li.append(
                    $('<a class="profiles_publication_link" />')
                      .attr('href', this.PublicationSource[0].PublicationSourceURL)
                      .text('View on ' + this.PublicationSource[0].PublicationSourceName)
                  );
                }

                $('#profiles_publications_list').append(li);
              });
            } else {
              $('#profiles_publications').hide();
            }

            if (data.AwardOrHonors && data.AwardOrHonors.length > 0) {
              $('#profiles_awards_list').remove();
              $('#profiles_awards')
                .show()
                .append($('<ul id="profiles_awards_list"></ul>'));

              jQuery.each(data.AwardOrHonors, function() {
                var li = $('<li />').append(this.Summary);
                $('#profiles_awards_list').append(li);
              });
            } else {
              $('#profiles_awards').hide();
            }

            $("html, body").animate({ scrollTop: 0 }, 100);
            $("[id^='profiles_']:visible").fadeIn(100).fadeOut(100).fadeIn(100);
          });
        }
      }
    }
  );
}

function highlight_profiles_content(seconds) {
  var ms = (seconds || 1) * 1000;
  $("[id^='profiles_']").addClass('highlighted');
  setTimeout(function() {
    $("[id^='profiles_']").removeClass('highlighted');
  }, ms);
}
</script>