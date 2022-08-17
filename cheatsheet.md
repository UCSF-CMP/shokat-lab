---
layout: page
title: markdown cheatsheet
permalink: /cheat/
published: false
---

Headers
# Heading
	H1
## Heading
	H2
### Heading
	H3
#### Heading
	H4
##### Heading
	H5
###### Heading
	H6

Inline HTML
<ul>list</ul>
	You can use the raw HTML in your Markdown

Emphasis
_Text_
	Displays text in italics
**Text**
  Displays the text in bold
**_Text_**
 	Displays the text in bold and italics
~~Text~~
	Adds strikethrough effect to the text

Images
![alt text](https://github.com/n48.png "Logo Title")
	Inline style

[alt text][logo]
The reference style. Reference need to be declared as [logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

Lists
1. item1
	First ordered list item
2. item2
	Second ordered list item
⋅⋅1. Item
	Ordered sub-list item
* Item
	Unordered list item
⋅⋅* Item
	Unordered sub-list item

  Code and Syntax Highlighting
  `code`
  	Inline code has back-ticks around it
  ``` Code blocks ```
  	Blocks of code are either fenced by lines with three back-ticks or are indented with four spaces

    Links
    [text link](https://duckduckgo.com)
    	Inline-style link
    [text link with title](https://duckduckgo.com "DDG Home")
    	Inline-style link with title
    [Reference-style link][Arbitrary case-insensitive reference text]
    	Reference style link
    [Use numbers for reference-style link definitions][1]
    	Links with a reference number. The number needs to be defined as [1]: http://slashdot.org

      Blockquotes
      > Blockquotes
      	Blockquotes are very handy in email to emulate reply text

        Horizontal Rule
      ---
      	You can get a horizontal rule by typing three or more hyphens (-), asterisks (*) or underscore (_) 
