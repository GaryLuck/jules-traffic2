## 2024-05-24 - Semantic Range Input Outputs
**Learning:** For custom slider displays where the current value of an `<input type="range">` is shown visually in text next to it, using a plain `<span>` element means screen readers won't automatically associate the displayed value with the input.
**Action:** Use an `<output>` element instead of a `<span>` and add a `for="inputId"` attribute. This binds the displayed value properly to the input, ensuring screen readers can politely announce changes. Also ensure that `<canvas>` elements have `role="img"` and `aria-label="..."` attributes so they aren't ignored or read out awkwardly by screen readers.
## 2024-05-25 - Hidden Interactions and Focus States
**Learning:** Hidden interactions (like clicking a canvas to add an item) are inaccessible to users who don't know they exist, and custom inputs/buttons lacking `:focus-visible` states are difficult for keyboard navigators to use.
**Action:** Always provide explicit visual affordances (helper text) for hidden click events, update `aria-label` to include instructions for screen readers, and ensure all interactive elements, including `<canvas>` elements if they are interactive, have clear `:focus-visible` styling and a `tabindex`.
## 2026-04-10 - Canvas Keyboard Accessibility
**Learning:** While simple `<canvas>` interaction (like clicking) is easily achievable, achieving functional parity for keyboard-only or screen reader users requires dedicated state management to track focus inside the canvas and dedicated key listeners (e.g., arrow keys) to navigate internal elements.
**Action:** When a canvas is interactive, always check if keyboard interactions (like Enter/Space) achieve the same fine-grained control as mouse clicks. If not, implement internal focus tracking (e.g., `selectedCell`), handle arrow keys for navigation, provide clear visual feedback for the selected area, and explicitly update `aria-label` instructions to guide users on how to use these controls.

## 2024-05-18 - Making Custom Canvas Elements Accessible
**Learning:** Custom interactive elements built with HTML Canvas are inherently opaque to screen readers because they lack the DOM structure that assistive technologies rely on. Standard ARIA roles on the canvas element only provide a general description.
**Action:** When creating complex internal interactions within a Canvas element (like navigating cells or adding elements to specific locations), use a visually hidden `aria-live="polite"` region to programmatically broadcast these state changes and interactions to screen reader users.
