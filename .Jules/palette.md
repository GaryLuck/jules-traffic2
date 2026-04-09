## 2024-05-24 - Semantic Range Input Outputs
**Learning:** For custom slider displays where the current value of an `<input type="range">` is shown visually in text next to it, using a plain `<span>` element means screen readers won't automatically associate the displayed value with the input.
**Action:** Use an `<output>` element instead of a `<span>` and add a `for="inputId"` attribute. This binds the displayed value properly to the input, ensuring screen readers can politely announce changes. Also ensure that `<canvas>` elements have `role="img"` and `aria-label="..."` attributes so they aren't ignored or read out awkwardly by screen readers.
## 2024-05-25 - Hidden Interactions and Focus States
**Learning:** Hidden interactions (like clicking a canvas to add an item) are inaccessible to users who don't know they exist, and custom inputs/buttons lacking `:focus-visible` states are difficult for keyboard navigators to use.
**Action:** Always provide explicit visual affordances (helper text) for hidden click events, update `aria-label` to include instructions for screen readers, and ensure all interactive elements, including `<canvas>` elements if they are interactive, have clear `:focus-visible` styling and a `tabindex`.
## 2024-11-20 - Canvas Keyboard Hint and ARIA Description
**Learning:** Users (and screen readers) miss out on existing keyboard shortcuts for interactive canvases if hints are missing entirely, and `aria-label`s can become too verbose if they mix description with interaction instructions.
**Action:** Use `aria-describedby` to link the canvas to a visually explicit hint that includes both mouse and keyboard instructions, keeping the `aria-label` concise.
