## 2024-05-24 - Semantic Range Input Outputs
**Learning:** For custom slider displays where the current value of an `<input type="range">` is shown visually in text next to it, using a plain `<span>` element means screen readers won't automatically associate the displayed value with the input.
**Action:** Use an `<output>` element instead of a `<span>` and add a `for="inputId"` attribute. This binds the displayed value properly to the input, ensuring screen readers can politely announce changes. Also ensure that `<canvas>` elements have `role="img"` and `aria-label="..."` attributes so they aren't ignored or read out awkwardly by screen readers.
## 2024-05-24 - Interactive Canvas Accessibility
**Learning:** When a `<canvas>` has mouse interactions (like clicking to add an item at a specific coordinate), it's completely invisible to keyboard users. Just adding `tabindex="0"` isn't enough; you must provide an equivalent keyboard interaction.
**Action:** Add a `keydown` listener (listening for Enter/Space) that performs a meaningful equivalent action (like adding the item to a random available spot) and clearly describe this alternative in the `aria-label` and visual hints.
