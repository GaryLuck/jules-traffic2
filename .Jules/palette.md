## 2024-05-24 - Semantic Range Input Outputs
**Learning:** For custom slider displays where the current value of an `<input type="range">` is shown visually in text next to it, using a plain `<span>` element means screen readers won't automatically associate the displayed value with the input.
**Action:** Use an `<output>` element instead of a `<span>` and add a `for="inputId"` attribute. This binds the displayed value properly to the input, ensuring screen readers can politely announce changes. Also ensure that `<canvas>` elements have `role="img"` and `aria-label="..."` attributes so they aren't ignored or read out awkwardly by screen readers.
## 2026-04-02 - Reveal hidden canvas interaction
**Learning:** Non-standard interactive elements like canvas often hide features because they lack native affordances like hover states or cursors.
**Action:** Added a visual text hint to explicitly describe the hidden interaction.
