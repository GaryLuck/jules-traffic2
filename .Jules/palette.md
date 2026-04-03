## 2024-05-24 - Semantic Range Input Outputs
**Learning:** For custom slider displays where the current value of an `<input type="range">` is shown visually in text next to it, using a plain `<span>` element means screen readers won't automatically associate the displayed value with the input.
**Action:** Use an `<output>` element instead of a `<span>` and add a `for="inputId"` attribute. This binds the displayed value properly to the input, ensuring screen readers can politely announce changes. Also ensure that `<canvas>` elements have `role="img"` and `aria-label="..."` attributes so they aren't ignored or read out awkwardly by screen readers.
## 2024-05-24 - Exposing Canvas Interactions
**Learning:** When an HTML `<canvas>` has interactive click features, it is hidden from keyboard navigation and screen readers because the internal state isn't mapped to the DOM.
**Action:** Provide a separate, semantic HTML control (like a `<button>`) to expose that functionality. This ensures discoverability and keyboard/screen-reader accessibility without compromising the canvas semantics.
