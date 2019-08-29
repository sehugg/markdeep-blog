const BLOG_NAME = "My Site";
function blog_navbar() {
  var navDiv = document.createElement("div");
  //navDiv.style.position = 'absolute';
  navDiv.innerHTML = `
<!-- navigation -->
<a href="/">Home</a> &gt; <a href="/blog">Blog</a>
  `;
  document.body.insertBefore(navDiv, document.body.firstChild);
  var h1 = document.querySelector("h1") || document.querySelector("h2");
  document.title = BLOG_NAME + " - " + (h1?h1.innerText:"");
  var footdiv = document.querySelector(".markdeepFooter");
  if (footdiv) {
    footdiv.innerHTML = `
    <h3>
      <a href="/blog/rss.xml">RSS</a>
      &#8226;
      <a href="/blog/feed.xml">Atom</a>
    </h3>
    <i>Formatted by MarkDeep.</i>
    `;
  }
  // Google Analytics
  if (window.location.host.endsWith('example.com')) {
    var ga = document.createElement('script');
    ga.type = 'text/javascript';
    ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('head')[0];
    s.appendChild(ga);
  }
}
// set onLoad
if (!window.markdeepOptions) window.markdeepOptions = {};
window.markdeepOptions.onLoad = blog_navbar;
// analytics
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-xxxxxxx-x']);
_gaq.push(['_anonymizeIp', 'true']);
_gaq.push(['_trackPageview']);
