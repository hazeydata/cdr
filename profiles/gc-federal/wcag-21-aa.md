# WCAG 2.1 Level AA — Developer Checklist

> **Standard:** [WCAG 2.1](https://www.w3.org/TR/WCAG21/)
> **Level:** AA (includes all Level A criteria)
> **GC Context:** Mandatory per [Standard on Web Accessibility](http://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=23601)
> **CDR Context:** Every tool built for a GC federal department must meet every item below

This is a practical, actionable checklist — not a theoretical overview. If you can check every box, you're WCAG 2.1 AA compliant.

---

## 1. Perceivable

### 1.1 Text Alternatives
- [ ] All `<img>` elements have `alt` attributes
- [ ] Informative images have descriptive alt text (describe what the image conveys)
- [ ] Decorative images have empty alt (`alt=""`) or are CSS backgrounds
- [ ] Complex images (charts, diagrams) have short alt + detailed description nearby
- [ ] Image buttons have alt describing the action ("Submit form"), not the appearance ("blue arrow")
- [ ] `<iframe>` elements have descriptive `title` attributes
- [ ] Icons used for functionality have screen-reader-accessible text (`aria-label` or visually hidden text)

### 1.2 Time-Based Media
- [ ] Pre-recorded video has synchronized captions (accurate, including speaker ID and sound effects)
- [ ] Pre-recorded audio has text transcript
- [ ] Pre-recorded video has audio description for visual-only content
- [ ] Live video/audio has real-time captions (AA)
- [ ] If no media is used, this section is N/A

### 1.3 Adaptable
- [ ] Headings use proper HTML tags (`<h1>`–`<h6>`), properly nested (no skipping levels)
- [ ] Lists use `<ul>`, `<ol>`, or `<dl>` elements
- [ ] Data tables use `<th>`, `<caption>`, and `scope` attributes
- [ ] Form fields have associated `<label>` elements (using `for`/`id`)
- [ ] Related form fields grouped with `<fieldset>` and `<legend>`
- [ ] Page regions identified with landmarks (`<nav>`, `<main>`, `<aside>`, `<header>`, `<footer>`)
- [ ] Reading/DOM order matches visual order
- [ ] Instructions don't rely solely on shape, size, position, or sound
- [ ] Content works in both portrait and landscape orientations *(2.1)*
- [ ] Form fields have appropriate `autocomplete` attributes for personal data *(2.1)*

### 1.4 Distinguishable
- [ ] Colour is never the only way to convey information (links, errors, status — always have a non-colour indicator)
- [ ] No audio auto-plays; if it must, provide pause/stop/volume controls
- [ ] Normal text contrast ratio: **4.5:1** minimum
- [ ] Large text (18pt+ or 14pt+ bold) contrast ratio: **3:1** minimum
- [ ] Text resizable to 200% without loss of content or functionality
- [ ] Use relative units (`rem`, `em`, `%`) for font sizes — not `px`
- [ ] Real text used instead of images of text (exception: logos)
- [ ] Content reflows at 320px width without horizontal scrolling *(2.1)*
- [ ] UI components and graphical elements: **3:1** contrast ratio minimum *(2.1)*
- [ ] No content loss when users override text spacing (line-height 1.5×, paragraph spacing 2×, letter spacing 0.12×, word spacing 0.16×) *(2.1)*
- [ ] Hover/focus-triggered content (tooltips, popups) is dismissible (Esc), hoverable, and persistent *(2.1)*

---

## 2. Operable

### 2.1 Keyboard Accessible
- [ ] **All** functionality available via keyboard (Tab, Shift+Tab, Enter, Space, Esc, arrows)
- [ ] Focus is never trapped in a component (except modals, which trap correctly and allow Esc to close)
- [ ] Custom widgets follow [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) keyboard patterns
- [ ] Drag-and-drop has keyboard alternative
- [ ] Single-character keyboard shortcuts can be turned off or remapped *(2.1)*

### 2.2 Enough Time
- [ ] No time limits unless essential; if time limits exist, user can turn off, adjust (10×), or extend
- [ ] Session timeouts provide warning and option to extend
- [ ] No auto-moving/blinking content lasting >5 seconds without pause control

### 2.3 Seizures
- [ ] No content flashes more than 3 times per second

### 2.4 Navigable
- [ ] "Skip to main content" link is the first focusable element
- [ ] Every page has a descriptive, unique `<title>` (pattern: "Page Name — Site Name")
- [ ] Tab order follows logical reading order (no `tabindex` > 0)
- [ ] Link text describes destination/action (no "click here" or naked "read more")
- [ ] At least two ways to find any page (nav, search, sitemap, etc.) (AA)
- [ ] Headings accurately describe their content (AA)
- [ ] All interactive elements have a **visible** focus indicator (AA)
- [ ] Focus indicator has minimum **3:1** contrast

### 2.5 Input Modalities *(2.1)*
- [ ] No multi-point or path-based gestures without single-pointer alternative
- [ ] Actions trigger on `click`/`mouseup`, not `mousedown` (pointer cancellation)
- [ ] Accessible name of components contains the visible label text
- [ ] No motion-triggered actions without UI alternative

---

## 3. Understandable

### 3.1 Readable
- [ ] `<html lang="en">` or `<html lang="fr">` set correctly
- [ ] Content in another language marked with `lang` attribute (critical for bilingual GC apps)

### 3.2 Predictable
- [ ] Focus changes don't cause unexpected context changes
- [ ] Form inputs don't auto-submit or cause unexpected navigation
- [ ] Navigation menus consistent across all pages (AA)
- [ ] Same-function components have consistent labels across pages (AA)

### 3.3 Input Assistance
- [ ] Form errors identified in text (not just colour), associated with the field (`aria-describedby` or `aria-errormessage`)
- [ ] Every form field has a visible label
- [ ] Required fields indicated (text, not just asterisk colour)
- [ ] Expected format shown (e.g., "YYYY-MM-DD")
- [ ] Error suggestions provided ("Date must be in YYYY-MM-DD format") (AA)
- [ ] Legal/financial/data submissions: provide review step or ability to undo (AA)

---

## 4. Robust

- [ ] HTML validates without significant errors (no duplicate `id`s, proper nesting)
- [ ] All UI components have accessible names
- [ ] Custom components have appropriate ARIA roles, states, and properties
- [ ] Dynamic content changes announced via `aria-live` regions
- [ ] Status messages (success, error, loading) announced to screen readers *(2.1)*

---

## Testing Protocol

Run these tests before submission:

### Automated Scans
- [ ] axe DevTools (browser extension) — zero violations at AA level
- [ ] Lighthouse accessibility audit — 90+ score
- [ ] WAVE evaluation tool — zero errors (warnings acceptable with justification)

### Manual Testing
- [ ] **Keyboard navigation:** Navigate entire app using only keyboard. Every function works.
- [ ] **Screen reader:** Test complete workflows with NVDA (Windows) or VoiceOver (macOS). All content announced correctly.
- [ ] **Zoom to 200%:** No content lost, no horizontal scroll at standard viewport
- [ ] **320px viewport:** Content reflows. No horizontal scroll (except complex tables/maps)
- [ ] **Contrast check:** Use browser DevTools or WebAIM Contrast Checker on all text and UI elements
- [ ] **Text spacing override:** Apply spacing overrides (bookmarklet available) — no content lost
- [ ] **Colour blindness simulation:** Use NoCoffee or browser built-in filters — all information still conveyed

### GC-Specific
- [ ] **Both language versions tested.** French version is equally accessible.
- [ ] **WET/GCWeb components used where possible.** They're pre-tested for WCAG 2.0 AA.
- [ ] **GC Design System components evaluated** for new projects (built for WCAG 2.1 AA).

---

## Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| Removing focus outlines with `outline: none` | Replace with a custom visible focus style |
| Using colour alone for error indication | Add icon, text label, or border change |
| Using `placeholder` as a label | Always use a visible `<label>` element |
| Skipping heading levels (`<h1>` → `<h3>`) | Use proper heading hierarchy |
| Using `<div>` or `<span>` for buttons | Use `<button>` or `<a>` — native HTML is accessible by default |
| Setting `tabindex="5"` to control order | Fix DOM order instead; only use `tabindex="0"` or `tabindex="-1"` |
| Auto-playing carousels without controls | Add pause/stop controls; better yet, don't use carousels |
| Hardcoded `px` font sizes | Use `rem` or `em` so users can resize |
| Links that say "click here" | Describe the destination: "View the HR dashboard" |
| Tables for layout | Use CSS Grid or Flexbox for layout; `<table>` for data only |

---

## References

- [WCAG 2.1 Specification](https://www.w3.org/TR/WCAG21/)
- [Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/)
- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/?levels=aaa)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [GC Standard on Web Accessibility](http://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=23601)
- [WET Accessibility](https://wet-boew.github.io/wet-boew/index-en.html)
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

---

*Every GC web application must meet WCAG 2.1 Level AA. Test thoroughly. No exceptions.*
