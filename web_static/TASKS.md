## Tasks to Complete

+ [x] 0. Inline styling<br/>_**[0-index.html](0-index.html)**_ contains an HTML page that displays a header and a footer.
  + Layout:
    + Body:
      + No margin.
      + No padding.
    + Header:
      + Color #FF0000 (red).
      + Height: 70px.
      + Width: 100%.
    + Footer:
      + Color #00FF00 (green).
      + Height: 60px.
      + Width: 100%.
      + Text `Best School` centered vertically and horizontally.
      + Always at the bottom at the page.
  + Requirements:
    + You must use the `header` and `footer` tags.
    + You are not allowed to import any files.
    + You are not allowed to use the `style` tag in the `head` tag.
    + Use inline styling for all your tags.

+ [x] 1. Head styling<br/>_**[1-index.html](1-index.html)**_ contains an HTML page that displays a header and a footer by using the `style` tag in the `head` tag (same as [0-index.html](0-index.html)).
  + Requirements:
    + You must use the `header` and `footer` tags.
    + You are not allowed to import any files.
    + No inline styling.
    + You must use the `style` tag in the `head` tag.
    + The layout must be exactly the same as [0-index.html](0-index.html).

+ [x] 2. CSS files<br/>_**[2-index.html](2-index.html)**_ contains an HTML page that displays a header and a footer by using CSS files (same as [1-index.html](1-index.html)).
  + Requirements:
    + You must use the `header` and `footer` tags.
    + No inline styling.
    + You must have 3 CSS files:
      + [styles/2-common.css](styles/2-common.css): for global style (i.e. the `body` style).
      + [styles/2-header.css](styles/2-header.css): for header style.
      + [styles/2-footer.css](styles/2-footer.css): for footer style.
    + The layout must be exactly the same as [1-index.html](1-index.html)

+ [x] 3. Zoning done!<br/>_**[3-index.html](3-index.html)**_ contains an HTML page that displays a header and footer by using CSS files (same as [2-index.html](2-index.html)).
  + Layout:
    + Common:
      + No margin.
      + No padding.
      + Font color: #484848.
      + Font size: 14px.
      + Font family: `Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;`.
      + [Icon](images/icon.png) in the browser tab.
    + Header:
      + Color: white.
      + Height: 70px.
      + Width: 100%.
      + Border bottom 1px #CCCCCC.
      + [Logo](images/logo.png) align on left and center vertically (20px space at the left).
    + Footer:
      + Color white.
      + Height: 60px.
      + Width: 100%.
      + Border top 1px #CCCCCC.
      + Text `Best School` center vertically and horizontally.
      + Always at the bottom at the page.
  + Requirements:
    + No inline style.
    + You are not allowed to use the `img` tag.
    + You are not allowed to use the `style` tag in the `head` tag.
    + All images must be stored in the `images` folder.
    + You must have 3 CSS files:
      + [styles/3-common.css](styles/3-common.css): for the global style (i.e `body` style).
      + [styles/3-header.css](styles/3-header.css): for the header style.
      + [styles/3-footer.css](styles/3-footer.css): for the footer style.

+ [x] 4. Search!<br/>_**[4-index.html](4-index.html)**_ contains an HTML page that displays a header, footer and a filters box with a search button.
  + Layout: (based on [3-index.html](3-index.html)).
    + Container:
      + Between `header` and `footer` tags, add a `div`:
        + Classname: `container`.
        + Max width 1000px.
        + Margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot).
    + Center horizontally.
    + Filter section:
      + Tag `section`.
      + Classname `filters`.
      + Inside the `.container`.
      + Color white.
      + Height: 70px.
      + Width: 100% of the container.
      + Border 1px #DDDDDD with radius 4px.
    + Button search:
      + Tag `button`.
      + Text `Search`.
      + Font size: 18px.
      + Inside the section filters.
      + Background color #FF5A5F.
      + Text color #FFFFFF.
      + Height: 48px.
      + Width: 20% of the section filters.
      + No borders.
      + Border radius: 4px.
      + Center vertically and at 30px of the right border.
      + Change opacity to 90% when the mouse is on the button.
  + Requirements:
    + You must use: `header`, `footer`, `section`, and `button` tags.
    + No inline style.
    + You are not allowed to use the `img` tag.
    + You are not allowed to use the `style` tag in the `head` tag.
    + All images must be stored in the `images` folder.
    + You must have 4 CSS files:
      + [styles/4-common.css](styles/4-common.css): for the global style (`body` and `.container` styles).
      + [styles/3-header.css](styles/3-header.css): for the header style.
      + [styles/3-footer.css](styles/3-footer.css): for the footer style.
      + [styles/4-filters.css](styles/4-filters.css): for the filters style.
    + [4-index.html](4-index.html) won’t be W3C valid and there's no need to worry since it’s temporary.

+ [x] 5. More filters<br/>_**[5-index.html](5-index.html)**_ contains an HTML page that displays a header, footer and a filters box.
  + Layout: (based on [4-index.html](4-index.html)).
    + Locations and Amenities filters:
      + Tag: `div`.
      + Classname: `locations` for location tag and `amenities` for the other.
      + Inside the section filters (same level as the `button` Search).
      + Height: 100% of the section filters.
      + Width: 25% of the section filters.
      + Border right #DDDDDD 1px only for the first left filter.
      + Contains a title:
        + Tag: `h3`.
        + Font weight: 600.
        + Text `States` or `Amenities`.
      + Contains a subtitle:
        + Tag: `h4`.
        + Font weight: 400.
        + Font size: 14px.
        + Text with fake contents.
  + Requirements:
    + You must use: `header`, `footer`, `section`, `button`, `h3`, and `h4` tags.
    + No inline style.
    + You are not allowed to use the `img` tag.
    + You are not allowed to use the `style` tag in the `head` tag.
    + All images must be stored in the `images` folder.
    + You must have 4 CSS files:
      + [styles/4-common.css](styles/4-common.css): for the global style (`body` and `.container` styles).
      + [styles/3-header.css](styles/3-header.css): for the header style.
      + [styles/3-footer.css](styles/3-footer.css): for the footer style.
      + [styles/5-filters.css](styles/5-filters.css): for the filters style.

+ [x] 6. It's (h)over<br/>_**[6-index.html](6-index.html)**_ contains an HTML page that displays a header, footer and a filters box with dropdown.
  + Layout: (based on [5-index.html](5-index.html)).
    + Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter `div`:
      + Tag `ul`.
      + Classname `popover`.
      + Text should be fake now.
      + Inside each `div`.
      + Not displayed by default.
      + Color #FAFAFA.
      + Width same as the `div` filter.
      + Border #DDDDDD 1px with border radius 4px.
      + No list display.
      + Location filter has 2 levels of `ul`/`li`:
        + State -> cities.
        + State name must be display in a `h2` tag (font size 16px).
  + Requirements:
    + You must use: `header`, `footer`, `section`, `button`, `h3`, `h4`, `ul`, and `li` tags.
    + No inline style.
    + You are not allowed to use the `img` tag.
    + You are not allowed to use the `style` tag in the `head` tag.
    + All images must be stored in the `images` folder.
    + You must have 4 CSS files:
      + [styles/4-common.css](styles/4-common.css): for the global style (`body` and `.container` styles).
      + [styles/3-header.css](styles/3-header.css): for the header style.
      + [styles/3-footer.css](styles/3-footer.css): for the footer style.
      + [styles/6-filters.css](styles/6-filters.css): for the filters style.

+ [x] 7. Display results<br/>_**[7-index.html](7-index.html)**_ contains an HTML page that displays a header, footer, a filters box with dropdown and results.
  + Layout: (based on [6-index.html](6-index.html)).
    + Add Places section:
      + Tag: `section`.
      + Classname: `places`.
        + Same level as the filters section, inside `.container`.
        + Contains a title:
        + Tag: `h1`.
        + Text: `Places`.
        + Align in the top left.
        + Font size: 30px.
      + Contains multiple “Places” as listing (horizontal or vertical) describe by:
      + Tag: `article`.
        + Width: 390px.
        + Padding and margin 20px.
        + Border #FF5A5F 1px with radius 4px.
        + Contains the place name:
          + Tag: `h2`.
          + Font size: 30px.
          + Center horizontally.
  + Requirements:
  + You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2`, `h3`, `h4`, `ul`, and `li` tags.
  + No inline style.
  + You are not allowed to use the `img` tag.
  + You are not allowed to use the `style` tag in the `head` tag.
  + All images must be stored in the `images` folder.
  + You must have 5 CSS files:
    + [styles/4-common.css](styles/4-common.css): for the global style (i.e. `body` and `.container` styles).
    + [styles/3-header.css](styles/3-header.css): for the header style.
    + [styles/3-footer.css](styles/3-footer.css): for footer style.
    + [styles/6-filters.css](styles/6-filters.css): for the filters style.
    + [styles/7-places.css](styles/7-places.css): for the places style.

+ [x] 8. More details<br/>_**[0-index.html](0-index.html)**_ contains an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.
  + Layout: (based on [7-index.html](7-index.html)).
    + Add more information to a Place `article`:
      + Price by night:
        + Tag: `div`.
        + Classname: `price_by_night`.
        + Same level as the place name.
        + Font color: #FF5A5F.
        + Border: #FF5A5F 4px rounded.
        + Min width: 60px.
        + Height: 60px.
        + Font size: 30px.
        + Align: the top right (with space).
      + Information section:
        + Tag: `div`.
        + Classname: `information`.
        + Height: 80px.
        + Border: top and bottom #DDDDDD 1px.
        + Contains (align vertically):
        + Number of guests:
          + Tag: `div`.
          + Classname: `max_guest`.
          + Width: 100px.
          + Fake text.
          + [Icon](images/icon_group.png).
        + Number of bedrooms:
          + Tag: `div`.
          + Classname: `number_rooms`.
          + Width: 100px.
          + Fake text.
          + [Icon](images/icon_bed.png).
        + Number of bathrooms:
          + Tag: `div`.
          + Classname: `number_bathrooms`.
          + Width: 100px.
          + Fake text.
          + [Icon](images/icon_bath.png).
      + User section:
        + Tag: `div`.
        + Classname: `user`.
        + Text `Owner: <fake text>`.
        + `Owner` text should be in bold.
      + Description section:
        + Tag: `div`.
        + Classname: `description`.
  + Requirements:
    + You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2`, `h3`, `h4`, `ul`, and `li` tags.
    + No inline style.
    + You are not allowed to use the `img` tag.
    + You are not allowed to use the `style` tag in the `head` tag.
    + All images must be stored in the `images` folder.
    + You must have 5 CSS files:
      + [styles/4-common.css](styles/4-common.css): for the global style (i.e. `body` and `.container` styles).
      + [styles/3-header.css](styles/3-header.css): for the header style.
      + [styles/3-footer.css](styles/3-footer.css): for the footer style.
      + [styles/6-filters.css](styles/6-filters.css): for the filters style.
      + [styles/8-places.css](styles/8-places.css): for the places style.

+ [x] 9. Full details<br/>_**[100-index.html](100-index.html)**_ contains an HTML page that displays a header, footer, a filters box with dropdown and results.
  + Layout: (based on [8-index.html](8-index.html))
    + Add more information to a Place `article`:
      + List of Amenities:
        + Tag `div`.
        + Classname `amenities`.
        + Margin top 40px.
        + Contains:
          + Title:
            + Tag `h2`.
            + Text `Amenities`.
            + Font size 16px.
            + Border bottom #DDDDDD 1px.
          + List of amenities:
            + Tag `ul` / `li`.
            + No list style.
            + Icons on the left: [Pet friendly](images/icon_pets.png), [TV](images/icon_tv.png), [Wifi](images/icon_wifi.png), etc... feel free to add more.
      + List of Reviews:
        + Tag `div`.
        + Classname `reviews`.
        + Margin top 40px.
        + Contains:
          + Title:
            + Tag `h2`.
            + Text `Reviews`.
            + Font size 16px.
            + Border bottom #DDDDDD 1px.
          + List of review:
            + Tag `ul` / `li`.
            + No list style.
            + A review is described by:
              + `h3` tag for the user/date description (font size 14px). Ex: "From Bob Dylan the 27th January 2017".
              + `p` tag for the text (font size 12px).
  + Requirements:
    + You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2`, `h3`, `h4`, `ul`, and `li` tags.
    + No inline style.
    + You are not allowed to use the `img` tag.
    + You are not allowed to use the `style` tag in the `head` tag.
    + All images must be stored in the `images` folder.
    + You must have 5 CSS files:
      + [styles/4-common.css](styles/4-common.css): for the global style (`body` and `.container` styles).
      + [styles/3-header.css](styles/3-header.css): for the header style.
      + [styles/3-footer.css](styles/3-footer.css): for the footer style.
      + [styles/6-filters.css](styles/6-filters.css): for the filters style.
      + [styles/100-places.css](styles/100-places.css): for the places style.

+ [x] 10. Flex<br/>Improve the Places section (from **task 9**) by using Flexible boxes for all Place articles.
  + Updated files: [101-index.html](101-index.html), [styles/4-common.css](styles/4-common.css), [styles/3-header.css](styles/3-header.css), [styles/3-footer.css](styles/3-footer.css), [styles/6-filters.css](styles/6-filters.css), and [styles/101-places.css](styles/101-places.css).

+ [x] 11. Responsive design<br/>Improve the page (from **task 10**) by adding responsive design to display correctly in mobile or small screens.
  + Examples:
    + No horizontal scrolling.
    + Redesign search bar depending of the width.
    + Etc.
  + Updated files: [102-index.html](102-index.html), [styles/102-common.css](styles/102-common.css), [styles/102-header.css](styles/102-header.css), [styles/102-footer.css](styles/102-footer.css), [styles/102-filters.css](styles/102-filters.css), and [styles/102-places.css](styles/102-places.css).

+ [x] 12. Accessibility<br/>Improve the page (from **task 11**) by adding Accessibility support.
  + Examples:
    + Colors contrast.
    + Header tags.
    + Etc.
  + Updated files: [103-index.html](103-index.html), [styles/103-common.css](styles/103-common.css), [styles/103-header.css](styles/103-header.css), [styles/103-footer.css](styles/103-footer.css), [styles/103-filters.css](styles/103-filters.css), and [styles/103-places.css](styles/103-places.css).
