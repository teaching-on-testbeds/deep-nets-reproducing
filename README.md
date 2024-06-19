## Deep Neural Nets: 33 years ago and 33 years from now

_Fraida Fund_

---

**Attribution**: This sequence of notebooks is adapted from the ICLR 2022 blog post ["Deep Neural Nets: 33 years ago and 33 years from now"](https://iclr-blog-track.github.io/2022/03/26/lecun1989/)  by Andrej Karpathy, and the associated [Github repository](https://github.com/karpathy/lecun1989-repro). 

---


In this sequence of experiments, you will reproduce a result from machine learning from 1989 - a paper that is possibly the earliest real-world application of a neural network trained end-to-end with backpropagation. (In earlier neural networks, some weights were actually hand-tuned!) You'll go a few steps further, though - after reproducing the results of the original paper, you'll get to use some modern 'tricks' to try and improve the performance of the model without changing its underlying infrastructure (i.e. no change in inference time!)

You can run this experiment on Google Colab: <a target="_blank" href="https://colab.research.google.com/github/teaching-on-testbeds/deep-nets-reproducing/blob/main/Deep_Neural_Nets_33_years_ago.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>



Or, you can use the Chameleon testbed: <a target="_blank" href="https://chameleoncloud.org/experiment/share/c0b5a325-b42c-4d44-bbb1-f2d9be7911d4">
  <img src='data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJMYXllcl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB3aWR0aD0iMTAwJSIgdmlld0JveD0iMCAwIDMwMCAyODciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDMwMCAyODciIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8cGF0aCBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTQ3LjAwMDAwMCwwLjk5OTk5OSAKCUMxOTguMjU5MTQwLDEuMDAwMDAwIDI0OS41MTgyNjUsMS4wMDAwMDAgMzAxLjAwMDAwMCwxLjAwMDAwMCAKCUMzMDEuMDAwMDAwLDUwLjM1NDAwNCAzMDEuMDAwMDAwLDk5LjcwODM0NCAzMDAuNjM3ODQ4LDE0OS42OTg3OTIgCglDMjk5LjQ5ODEzOCwxNDguNTg2MzA0IDI5OC41MjI4MjcsMTQ2Ljg5NzA0OSAyOTcuOTc3MzI1LDE0NS4wNzg4NTcgCglDMjk1LjY0NDY1MywxMzcuMzA0MTM4IDI5MS4zNzkxNTAsMTMwLjQ5OTg3OCAyODUuNTEzNTgwLDEyNS4yNDgxMzggCglDMjcxLjQ5ODY4OCwxMTIuNjk5ODM3IDI1NC45ODcxMzcsMTA4LjY1MjkwOCAyMzYuMTYwMzg1LDExMC43NzQ1MTMgCglDMjEzLjAzODQyMiwxMTMuMzgwMTY1IDE5My45Nzc2MDAsMTM0LjAwMTIyMSAxOTQuNjcyMDI4LDE1OC40NzgwMjcgCglDMTk1LjMzODg4MiwxODEuOTgzMjkyIDIxNi41MjU5ODYsMjAxLjE5MTMzMCAyNDEuMDk3NTM0LDE5NC45Mjg0ODIgCglDMjUyLjYxMTgzMiwxOTEuOTkzNjk4IDI1OS45NTcyNzUsMTg0LjA1NDk5MyAyNjIuNTA0NTQ3LDE3Mi43MDA4NjcgCglDMjY0LjcwOTc3OCwxNjIuODcxNDc1IDI2Mi4zOTI3MDAsMTUzLjc5NjcwNyAyNTQuMjkxMTUzLDE0Ni42OTM4MTcgCglDMjQ4LjA3NDU3MCwxNDEuMjQzNTE1IDIzOC40NTUzMDcsMTQwLjQwMjg2MyAyMzEuOTY0NjAwLDE0My4xOTYzODEgCglDMjI0LjM5MDk3NiwxNDYuNDU1OTYzIDIyMC4yMTIzNTcsMTUyLjY4MTg1NCAyMjEuMDc1MTY1LDE2MS4zNTYxNzEgCglDMjIxLjIyNzUyNCwxNjIuODg3OTg1IDIyMi4yODcyOTIsMTY1LjU0NjA1MSAyMjMuMDM4MDU1LDE2NS41ODU0MTkgCglDMjI1Ljg3MTk5NCwxNjUuNzMzOTk0IDIyNS45NzM2NjMsMTYzLjQyMTA1MSAyMjYuMDU1Mzg5LDE2MS4wODY5MjkgCglDMjI2LjIzODU3MSwxNTUuODU0OTUwIDIzMC4xODc0ODUsMTUwLjgyNjA1MCAyMzQuNDA2ODMwLDE1MC4wNDY5OTcgCglDMjQ2LjQ1OTUxOCwxNDcuODIxNjA5IDI1NS4wNzI2MDEsMTU3Ljc2NjcwOCAyNTEuMTgxNTQ5LDE2OS40NzIzMzYgCglDMjQ4LjMzNTA5OCwxNzguMDM1NDMxIDI0Mi4wMzYyMDksMTgxLjE1NTgwNyAyMzQuNTM4NDgzLDE4MS44MDc0NjUgCglDMjI3LjE2MDc1MSwxODIuNDQ4NjY5IDIxNy4xOTY1NDgsMTc1LjA4NDYyNSAyMTQuNDY5MzE1LDE2Ny45NDA4ODcgCglDMjA5LjY3NjE0NywxNTUuMzg1NjM1IDIxNy44MTM5MDQsMTM4LjM3NDY5NSAyMzAuNTkwNDM5LDEzMy45Njk3NDIgCglDMjM3LjQ5OTgzMiwxMzEuNTg3NjAxIDI0NC4zNTA4OTEsMTMyLjAxMjk4NSAyNTEuNTA1MTg4LDEzMi44NjQ3NDYgCglDMjcwLjQxODk3NiwxMzUuMTE2NTkyIDI4MC4zNzQ3NTYsMTQ4LjYxMjEyMiAyODAuODgyNTk5LDE2NS40NjAxNzUgCglDMjgxLjQzNzUzMSwxODMuODcxMTA5IDI3My44ODE1MzEsMjAwLjAzNTc2NyAyNjQuOTA4MjY0LDIxNS41Mjg3OTMgCglDMjU2Ljg2NzgyOCwyMjkuNDExMjQwIDI0NS45MDAxNDYsMjQwLjcwNzQxMyAyMzIuNjk3NzIzLDI1MC4xMzg4NTUgCglDMjMxLjkzNDgxNCwyNTAuNDIzNzIxIDIzMS40NzQxNjcsMjUwLjczOTA3NSAyMzEuMDI1NjgxLDI1MS4wNTMwNzAgCglDMjMxLjAzNzg0MiwyNTEuMDUxNzEyIDIzMS4wNDY1MzksMjUxLjAyODgzOSAyMzAuNjc5OTQ3LDI1MS4wNTAwMTggCglDMjI1LjA1MDA5NSwyNTMuNDM4OTA0IDIxOS45MjY1MTQsMjU2LjIxMjA5NyAyMTQuNDkyNDYyLDI1OC4wODQwNzYgCglDMjA1LjE2NTAyNCwyNjEuMjk3MjcyIDE5NS43MzU4MjUsMjYzLjQyODcxMSAxODUuNTM5ODEwLDI2Mi4zMDA5MzQgCglDMTc2Ljc5NzY4NCwyNjEuMzMzOTU0IDE2OC45NzQ0NzIsMjU4LjMwNDMyMSAxNjAuOTAyNDA1LDI1NC42NzY4MTkgCglDMTU2LjgzODE1MCwyNTEuNTg3MDA2IDE1Mi45NzY5NDQsMjQ4Ljc3MzMxNSAxNDguOTU0MzE1LDI0NS42NjU4OTQgCglDMTQ2LjIzNDA3MCwyNDIuOTAxNjcyIDE0My42NzUyNDcsMjQwLjQzMTE2OCAxNDAuOTUyNjA2LDIzNy42NjA0MTYgCglDMTM4LjIzNjQ5NiwyMzMuOTM1NjY5IDEzNS42ODQxODksMjMwLjUxMTE2OSAxMzMuNTMxNjQ3LDIyNy4wNTE0MjIgCglDMTM2Ljg5OTQ2MCwyMjYuNDE4NDQyIDEzOS44Njc0NzcsMjI1LjgyMDcwOSAxNDMuMDc0ODI5LDIyNS4xNzQ3NzQgCglDMTQ1LjA5ODY5NCwyMzAuNzA1MTA5IDE0OS4wMjA0NDcsMjMyLjY3MjU3NyAxNTQuNjkwNjEzLDIzMS43NjMzNjcgCglDMTU0LjY5MDYxMywyMzAuMTA5MDM5IDE1NC42OTA2MTMsMjI4LjcxODUyMSAxNTQuNjkwNjEzLDIyNy4xNTc2MzkgCglDMTUyLjc4MzU1NCwyMjcuMDQ3NzI5IDE1MS4xNTg1ODUsMjI2Ljk1NDA3MSAxNDkuNDg0NTEyLDIyNi44NTc1NzQgCglDMTQ5LjEwMjc1MywyMjUuMzM1NDk1IDE0OC4wODg3NjAsMjIzLjY0MzU1NSAxNDguNTU1MjUyLDIyMi42MzkzODkgCglDMTQ5LjM5OTc1MCwyMjAuODIxNjA5IDE1MC45NzI4MzksMjE5LjIzNDMxNCAxNTIuNTM0OTU4LDIxNy44OTIwNTkgCglDMTUzLjc4ODE0NywyMTYuODE1MjkyIDE1Ni44NDIwNTYsMjE1Ljk2NTI0MCAxNTYuNzQ1OTU2LDIxNS40OTMwNTcgCglDMTU2LjE1OTc0NCwyMTIuNjEyNzc4IDE1NS42NzE2MTYsMjA4LjkxODgwOCAxNTMuNjgzMDkwLDIwNy4zMDc4MTYgCglDMTUwLjg1ODA0NywyMDUuMDE5MTA0IDE0My42NDk1MjEsMjA3LjM5NDQ1NSAxNDEuOTgxMDE4LDIxMC43NDY2MTMgCglDMTQwLjc5MzM2NSwyMTMuMTMyNjkwIDE0MC43NjY0NzksMjE2LjA5NjU3MyAxNDAuMjA2MDg1LDIxOC44Nzk0NTYgCglDMTM2LjUxMTQ1OSwyMTkuMjI1MTQzIDEzMi43NjU1MTgsMjE5LjU3NTYyMyAxMjguODc5NzAwLDIxOS42MDY3OTYgCglDMTI2Ljg2NTU3OCwyMTUuODQ1NDkwIDEyNC45OTEzNDEsMjEyLjQwMzUwMyAxMjMuMDQ5NjA2LDIwOC41ODkyNzkgCglDMTE1LjQzMDc3OSwxODkuODk1MzI1IDExMS41NDc0MzIsMTcwLjg1ODg1NiAxMTEuODk5NzczLDE1MC41Nzc0MzggCglDMTEyLjM1MTYzOSwxNDYuMTA3ODE5IDExMi43Mzg1MTgsMTQyLjA3MDQ1MCAxMTMuNDIyOTEzLDEzNy43OTk1MDAgCglDMTE0LjE4NjQ2MiwxMzUuMDU3NjkzIDExNC42NTI1MDQsMTMyLjU0OTQ1NCAxMTUuMzg4MzI5LDEyOS44NjAxNTMgCglDMTE2LjA1NzgwOCwxMjguNDYyOTk3IDExNi40NTc0OTcsMTI3LjI0Njg5NSAxMTYuOTMwNzEwLDEyNS44MDY1MTEgCglDMTE3LjAwNDI0MiwxMjUuNTgyMjMwIDExNy4xMDc5MTAsMTI1LjEyMTY5NiAxMTcuNDk3ODc5LDEyNS4wOTI4ODggCglDMTIwLjQyNjE3MCwxMjUuNTgzNjQ5IDEyMS4xMTM4OTIsMTI3LjE0MjgxNSAxMjEuMTAzODgyLDEyOS42Njc0NTAgCglDMTIxLjA5NjY4NywxMzEuNDc5Mzg1IDEyMS45MDY2OTMsMTMzLjM1ODQxNCAxMjIuNjIyMjc2LDEzNS4wOTYyODMgCglDMTI0LjE4ODMwMSwxMzguODk5NTk3IDEyNy42NjA1MDAsMTM3LjkwNTg1MyAxMzAuNjM2NzQ5LDEzOC4wMTk1MDEgCglDMTMxLjkzNTM2NCwxMzguMDY5MDYxIDEzNC4wNDkxOTQsMTM4LjM0NzM4MiAxMzQuMzcwODgwLDEzNy43NTI2NzAgCglDMTM0Ljk3NDg1NCwxMzYuNjM2MTM5IDEzNC41NDQ4NjEsMTM0Ljk2MDMxMiAxMzQuNTQ0ODYxLDEzMy45NDM2NjUgCglDMTM1LjM1NTQyMywxMzIuNTE3NjcwIDEzNi4xMjUzMDUsMTMxLjE2MzIyMyAxMzYuODk1MjAzLDEyOS44MDg3NzcgCglDMTM1LjY3MTI5NSwxMjkuMjA1OTMzIDEzNC40MzQ3ODQsMTI4LjA3MjE1OSAxMzMuMjI1ODQ1LDEyOC4xMDA4MTUgCglDMTI5Ljc0MDMxMSwxMjguMTgzNDcyIDEyOS4wMzIzMDMsMTI2LjExNTY2MiAxMjkuMDMzNTg1LDEyMy40MDA5MDIgCglDMTI5LjAzNDkxMiwxMjAuNTc1NDcwIDEzMC4wMTU0NDIsMTE4LjU3MDgwOCAxMzMuNDIxOTk3LDExOC45NjY2NDQgCglDMTM0LjE3NDM5MywxMTkuMDU0MDcwIDEzNC45Njk3NDIsMTE4Ljc3MTg2NiAxMzYuMDM4ODY0LDExOC42MTc0ODUgCglDMTM1Ljg5MDA5MSwxMTYuOTM4ODQzIDEzNS43Njc0NTYsMTE1LjU1NTEyMiAxMzUuNjgwMjUyLDExNC41NzExNjcgCglDMTI5LjY0MjA0NCwxMTIuNDg5OTIyIDEyNi4wOTQzNjgsMTE1LjEzMjk1MCAxMjMuODYzNzM5LDExOS41NTIwNDggCglDMTIyLjM3NDM4MiwxMTkuMjk2NDMyIDEyMS4yNTQxOTYsMTE5LjEwNDE4NyAxMjAuMjM0OTc4LDExOC41OTA3NzUgCglDMTI1LjI2MjgxMCwxMTIuODU5MTY5IDEzMC4xODk2ODIsMTA3LjQ0ODcyMyAxMzUuNDc5ODg5LDEwMS45OTgyNDUgCglDMTM4LjI4MTYwMSwxMDAuOTc0OTA3IDE0MC43MTk5NzEsOTkuOTkxNTg1IDE0My41MjIyMTcsOTguOTgyNjY2IAoJQzE0OS45ODAwNzIsOTYuNjA1MTEwIDE1Ni4wMDcxNzIsOTQuMDU4NjQ3IDE2Mi4xODAxNDUsOTEuOTM2NTM5IAoJQzE4My4yNjU3NzgsODQuNjg3ODUxIDIwNC45MTAyOTQsNzkuODI3MzAxIDIyNy4wMTkyMjYsNzYuOTI1MDU2IAoJQzIzMS44ODQ2NDQsNzYuMjg2MzY5IDIzNi4yMjU2MDEsNzQuMzM0NzYzIDIzOC4wMzY3NTgsNjguNjEyMzIwIAoJQzI0MC44OTk1OTcsNjEuMDQ3OTEzIDIzNy41NjM3ODIsNTUuNDkwODk0IDIzMi45ODQyODMsNTAuNTY2MTIwIAoJQzIyMS42MjEwNjMsMzguMzQ2MTk1IDIwNy44MzE3MjYsMjkuNDE5NDI2IDE5My4wNDkyMjUsMjEuOTIyOTY2IAoJQzE5My4wMjE5NzMsMjEuOTcxMjMwIDE5My4xMTc3OTgsMjIuMDI2OTQ5IDE5My4wMzAwNjAsMjEuNzgxODA5IAoJQzE5Mi42NDU3NTIsMjEuNDEyMTY3IDE5Mi4zNDkxNTIsMjEuMjg3NjY2IDE5MS43MzI2MDUsMjEuMDA4NDQwIAoJQzE4OS4zMDYzNTEsMTkuODkyODgzIDE4Ny4yMDAwNTgsMTguOTMyMDUzIDE4NC45MTY3MTgsMTcuNjYxMjQzIAoJQzE3My4xNjI0NDUsMTIuNzM4MzM2IDE2MS41NzIyMzUsOC4xNTcyOTcgMTUwLjAyODA2MSwzLjQ2MzA3NyAKCUMxNDguODc1NDI3LDIuOTk0Mzg3IDE0OC4wMDI2NTUsMS44Mzc0OTIgMTQ3LjAwMDAwMCwwLjk5OTk5OSAKeiIvPgo8cGF0aCBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMzAxLjAwMDAwMCwxODUuMDAwMDAwIAoJQzMwMS4wMDAwMDAsMjE5LjMxNDg4MCAzMDEuMDAwMDAwLDI1My42Mjk3NjEgMzAxLjAwMDAwMCwyODcuOTcyMzIxIAoJQzIwMS4wNzIyMjAsMjg3Ljk3MjMyMSAxMDEuMTQ0NDMyLDI4Ny45NzIzMjEgMS4xMDgzMjEsMjg3Ljk3MjMyMSAKCUMxLjEwODMyMSwxOTIuNDU3MDc3IDEuMTA4MzIxLDk2LjkxNDAwOSAxLjEwODMyMSwxLjAwMDAwMCAKCUM0Mi4wMjAxNDksMS4wMDAwMDAgODMuMDQxNDEyLDEuMDAwMDAwIDEyNC44ODg1MzUsMS4xODY2MTYgCglDMTIzLjU3MTQxOSw0LjMzNzQzMyAxMjUuNjg1MDIwLDYuMzU3ODU5IDEyNy4xMzg1MDQsOC43MDYyNTYgCglDMTMwLjIxMjE0MywxMy42NzIzNTIgMTMzLjA0MTY4NywxOC43ODk1MzIgMTM1LjYxODQzOSwyNC4wNDIxODkgCglDMTI4LjE0Mzg2MCwyNi4xMjk1MzggMTIxLjAyMjE5NCwyOC4wMTk0MzYgMTEzLjUxMjYzNCwyOS45NDc1NjMgCglDMTA1LjY2OTM4MCwzMy4yMTA3MzkgOTcuOTYwMzA0LDM1Ljk1NzIyNiA5MC44MDYzNTEsMzkuNzUwNjE4IAoJQzY5LjYxNDQ1Niw1MC45ODc2NTYgNTMuNjA2NjEzLDY3LjY5ODkxNCA0Mi4xOTY0OTksODguNjIxNTUyIAoJQzI4LjUyODU0MywxMTMuNjg0MzY0IDIzLjgwMzM2NCwxNDAuNDEwNjYwIDI3Ljg1MzE0NiwxNjguODYwMTg0IAoJQzMwLjM0MjEyOSwxODYuMzQ1MTY5IDM1Ljg0ODQ5OSwyMDIuNjUyMzkwIDQ1LjI2MTkyNSwyMTcuMzU2OTQ5IAoJQzYwLjI4ODk4NiwyNDAuODMwNDkwIDgwLjAwODE2MywyNTkuMDQzNjEwIDEwNy4yMTYyMzIsMjY4LjQ2MzU5MyAKCUMxMzcuMzA0MDkyLDI4MS40MDM5OTIgMTY4LjA3NDUyNCwyODcuNDc5MTU2IDIwMC41OTY4NDgsMjgyLjEwMTM3OSAKCUMyMzAuNjkxMjM4LDI3Ny4xMjUwNjEgMjU0LjgzMDA5MywyNjIuMTc2Nzg4IDI3My41Nzc2OTgsMjM4LjU3MzMwMyAKCUMyODUuNjc5NzE4LDIyMy4zMzY2NzAgMjk0LjI5MDcxMCwyMDYuMTE0ODIyIDI5OS4wNjE3MDcsMTg3LjEwNjY1OSAKCUMyOTkuMjY1ODM5LDE4Ni4yOTM1MTggMzAwLjMzNDIyOSwxODUuNjk3MjgxIDMwMS4wMDAwMDAsMTg1LjAwMDAwMCAKeiIvPgo8cGF0aCBmaWxsPSIjNjM5QjRFIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMjMyLjk5OTk4NSwyNTAuMTY5MzEyIAoJQzI0NS45MDAxNDYsMjQwLjcwNzQxMyAyNTYuODY3ODI4LDIyOS40MTEyNDAgMjY0LjkwODI2NCwyMTUuNTI4NzkzIAoJQzI3My44ODE1MzEsMjAwLjAzNTc2NyAyODEuNDM3NTMxLDE4My44NzExMDkgMjgwLjg4MjU5OSwxNjUuNDYwMTc1IAoJQzI4MC4zNzQ3NTYsMTQ4LjYxMjEyMiAyNzAuNDE4OTc2LDEzNS4xMTY1OTIgMjUxLjUwNTE4OCwxMzIuODY0NzQ2IAoJQzI0NC4zNTA4OTEsMTMyLjAxMjk4NSAyMzcuNDk5ODMyLDEzMS41ODc2MDEgMjMwLjU5MDQzOSwxMzMuOTY5NzQyIAoJQzIxNy44MTM5MDQsMTM4LjM3NDY5NSAyMDkuNjc2MTQ3LDE1NS4zODU2MzUgMjE0LjQ2OTMxNSwxNjcuOTQwODg3IAoJQzIxNy4xOTY1NDgsMTc1LjA4NDYyNSAyMjcuMTYwNzUxLDE4Mi40NDg2NjkgMjM0LjUzODQ4MywxODEuODA3NDY1IAoJQzI0Mi4wMzYyMDksMTgxLjE1NTgwNyAyNDguMzM1MDk4LDE3OC4wMzU0MzEgMjUxLjE4MTU0OSwxNjkuNDcyMzM2IAoJQzI1NS4wNzI2MDEsMTU3Ljc2NjcwOCAyNDYuNDU5NTE4LDE0Ny44MjE2MDkgMjM0LjQwNjgzMCwxNTAuMDQ2OTk3IAoJQzIzMC4xODc0ODUsMTUwLjgyNjA1MCAyMjYuMjM4NTcxLDE1NS44NTQ5NTAgMjI2LjA1NTM4OSwxNjEuMDg2OTI5IAoJQzIyNS45NzM2NjMsMTYzLjQyMTA1MSAyMjUuODcxOTk0LDE2NS43MzM5OTQgMjIzLjAzODA1NSwxNjUuNTg1NDE5IAoJQzIyMi4yODcyOTIsMTY1LjU0NjA1MSAyMjEuMjI3NTI0LDE2Mi44ODc5ODUgMjIxLjA3NTE2NSwxNjEuMzU2MTcxIAoJQzIyMC4yMTIzNTcsMTUyLjY4MTg1NCAyMjQuMzkwOTc2LDE0Ni40NTU5NjMgMjMxLjk2NDYwMCwxNDMuMTk2MzgxIAoJQzIzOC40NTUzMDcsMTQwLjQwMjg2MyAyNDguMDc0NTcwLDE0MS4yNDM1MTUgMjU0LjI5MTE1MywxNDYuNjkzODE3IAoJQzI2Mi4zOTI3MDAsMTUzLjc5NjcwNyAyNjQuNzA5Nzc4LDE2Mi44NzE0NzUgMjYyLjUwNDU0NywxNzIuNzAwODY3IAoJQzI1OS45NTcyNzUsMTg0LjA1NDk5MyAyNTIuNjExODMyLDE5MS45OTM2OTggMjQxLjA5NzUzNCwxOTQuOTI4NDgyIAoJQzIxNi41MjU5ODYsMjAxLjE5MTMzMCAxOTUuMzM4ODgyLDE4MS45ODMyOTIgMTk0LjY3MjAyOCwxNTguNDc4MDI3IAoJQzE5My45Nzc2MDAsMTM0LjAwMTIyMSAyMTMuMDM4NDIyLDExMy4zODAxNjUgMjM2LjE2MDM4NSwxMTAuNzc0NTEzIAoJQzI1NC45ODcxMzcsMTA4LjY1MjkwOCAyNzEuNDk4Njg4LDExMi42OTk4MzcgMjg1LjUxMzU4MCwxMjUuMjQ4MTM4IAoJQzI5MS4zNzkxNTAsMTMwLjQ5OTg3OCAyOTUuNjQ0NjUzLDEzNy4zMDQxMzggMjk3Ljk3NzMyNSwxNDUuMDc4ODU3IAoJQzI5OC41MjI4MjcsMTQ2Ljg5NzA0OSAyOTkuNDk4MTM4LDE0OC41ODYzMDQgMzAwLjYzNzg0OCwxNTAuMTY3NDUwIAoJQzMwMS4wMDAwMDAsMTU4LjM1NDIzMyAzMDEuMDAwMDAwLDE2Ni43MDg0NjYgMzAwLjcwNjE3NywxNzUuNzIxNzEwIAoJQzI5OS43MTc4MDQsMTc4LjAzNjcyOCAyOTguODg0NjQ0LDE3OS42NDkyMTYgMjk4LjM0OTE4MiwxODEuMzU1MTY0IAoJQzI4OC40MzgzMjQsMjEyLjkzMTI1OSAyNzEuNjA2OTAzLDIzOS44NDM3MzUgMjQzLjg2MjUwMywyNTguNTk2NjQ5IAoJQzIwNi40Mjg5NzAsMjgzLjg5ODY1MSAxNjUuNjcyMDczLDI4My4xNzM4NTkgMTI0LjM4MDk5NywyNzIuMTE0OTkwIAoJQzEyNi42NTE4MTAsMjcyLjEzMTk4OSAxMjguNDg0ODYzLDI3Mi4wOTk2NDAgMTMwLjI5NzcyOSwyNzIuMjc1NDIxIAoJQzEzOS4zNDg1NzIsMjczLjE1Mjk1NCAxNDguNDU4Mzg5LDI3NS4yMjY4OTggMTU3LjQyNjAyNSwyNzQuNzIyMTk4IAoJQzE2OS45MjA3NjEsMjc0LjAxOTEwNCAxODIuNDcwMjkxLDI3Mi4xMTY4MjEgMTk0LjY4MTkxNSwyNjkuMzQzMjkyIAoJQzIwMi40MTUwNTQsMjY3LjU4Njg4NCAyMDkuNTc1OTI4LDI2My4zMTA5NzQgMjE3LjMwNzQ5NSwyNTkuOTk2ODg3IAoJQzIyMi4wOTY1MjcsMjU2Ljg5NTQ0NyAyMjYuNTcxNTMzLDI1My45NjIxNDMgMjMxLjA0NjUzOSwyNTEuMDI4ODM5IAoJQzIzMS4wNDY1MzksMjUxLjAyODgzOSAyMzEuMDM3ODQyLDI1MS4wNTE3MTIgMjMxLjMxNDY5NywyNTEuMDcyNDE4IAoJQzIzMi4wNjEwMzUsMjUwLjc4NTE4NyAyMzIuNTMwNTAyLDI1MC40NzcyNDkgMjMyLjk5OTk4NSwyNTAuMTY5MzEyIAp6Ii8+CjxwYXRoIGZpbGw9IiM2RUIyNTMiIG9wYWNpdHk9IjEuMDAwMDAwIiBzdHJva2U9Im5vbmUiIAoJZD0iCk0xMzUuOTcxMzU5LDIzLjg0NDczOCAKCUMxMzMuMDQxNjg3LDE4Ljc4OTUzMiAxMzAuMjEyMTQzLDEzLjY3MjM1MiAxMjcuMTM4NTA0LDguNzA2MjU2IAoJQzEyNS42ODUwMjAsNi4zNTc4NTkgMTIzLjU3MTQxOSw0LjMzNzQzMyAxMjUuMzU3MTkzLDEuMTg2NjE2IAoJQzEzMi4wMjA5NTAsMS4wMDAwMDAgMTM5LjA0MTkwMSwxLjAwMDAwMCAxNDYuNTMxNDMzLDAuOTk5OTk5IAoJQzE0OC4wMDI2NTUsMS44Mzc0OTIgMTQ4Ljg3NTQyNywyLjk5NDM4NyAxNTAuMDI4MDYxLDMuNDYzMDc3IAoJQzE2MS41NzIyMzUsOC4xNTcyOTcgMTczLjE2MjQ0NSwxMi43MzgzMzYgMTg0LjQ3NTY0NywxNy42NjQ1ODUgCglDMTc3Ljg2Mjk2MSwxNy41MDA1NzQgMTcyLjY4MDkyMywxOS41MjA4MDMgMTY5LjU1OTg0NSwyNS4zMTQyMzYgCglDMTY3LjA4MTc3MiwyOS45MTQxMjUgMTY3LjE2ODcxNiwzNC44NDExOTQgMTcwLjA3MTc0NywzOS4wNTkxMTYgCglDMTcyLjMxMzg1OCw0Mi4zMTY3NDYgMTc0LjgyODAxOCw0Ni4xOTMzNDQgMTgwLjQzMzY1NSw0NC45NzkzMjQgCglDMTg1LjA1OTA5Nyw0NS43OTUwMDIgMTg4LjEwNjY0NCw0My42NTc2MTIgMTkxLjI2OTUxNiw0MC44NjczNTUgCglDMTk2LjExODc1OSwzNy44NzE4MDcgMTk2LjQ0NTYzMywzMy40OTYzNDYgMTk1LjUyOTI5NywyOC45MDIzNDggCglDMTk1LjA0ODY0NSwyNi40OTI1OTIgMTkzLjkxNTE2MSwyNC4yMTMwNDkgMTkzLjA3NjQ3NywyMS44NzQ3MDIgCglDMjA3LjgzMTcyNiwyOS40MTk0MjYgMjIxLjYyMTA2MywzOC4zNDYxOTUgMjMyLjk4NDI4Myw1MC41NjYxMjAgCglDMjM3LjU2Mzc4Miw1NS40OTA4OTQgMjQwLjg5OTU5Nyw2MS4wNDc5MTMgMjM3LjYyMzIxNSw2OC42Mjc0MTEgCglDMjM1LjM2NTE0Myw2OS4yMzIyODUgMjMzLjcxNDEyNyw2OS40MTIwNjQgMjMyLjA4MDU4Miw2OS42OTMzMzYgCglDMjE0LjM0MjQ4NCw3Mi43NDc1MTMgMTk2LjUzNzkzMyw3NC41OTA4NDMgMTc4LjU4NTQ4MCw3MS44OTQyNDEgCglDMTcxLjg4NjEwOCw3MC44ODc5NDcgMTY2LjUwNDU2Miw2Ny45Mzg3MjEgMTYzLjU1MjAwMiw2MS4xNDk5MjkgCglDMTYxLjA1NTEzMCw1NS40MDg4NzUgMTUzLjg1NzgxOSw1NC42NjgzMzEgMTQ5LjU1MTMxNSw1OS4xODQ5MzcgCglDMTQ4LjU0NjgxNCw2MC4yMzg0NDEgMTQ3LjMwNDUzNSw2MS4wNjUyMzUgMTQ2LjEyMjIwOCw2MS41NzAwMTUgCglDMTQ1LjMwMzg2NCw1NS43NTQyNDIgMTQ1LjEwNDk4MCw1MC4yMDI1MTUgMTQzLjYyODEyOCw0NS4wMTQ1OTEgCglDMTQxLjU3ODU1MiwzNy44MTQ4NjkgMTM4LjU2OTU4MCwzMC44ODgyNjggMTM1Ljk3MTM1OSwyMy44NDQ3MzggCnoiLz4KPHBhdGggZmlsbD0iIzRGNzg0MSIgb3BhY2l0eT0iMS4wMDAwMDAiIHN0cm9rZT0ibm9uZSIgCglkPSIKTTEyMy45MzM5MzcsMjcyLjE2MTU2MCAKCUMxNjUuNjcyMDczLDI4My4xNzM4NTkgMjA2LjQyODk3MCwyODMuODk4NjUxIDI0My44NjI1MDMsMjU4LjU5NjY0OSAKCUMyNzEuNjA2OTAzLDIzOS44NDM3MzUgMjg4LjQzODMyNCwyMTIuOTMxMjU5IDI5OC4zNDkxODIsMTgxLjM1NTE2NCAKCUMyOTguODg0NjQ0LDE3OS42NDkyMTYgMjk5LjcxNzgwNCwxNzguMDM2NzI4IDMwMC43MDYxNzcsMTc2LjE5MDM2OSAKCUMzMDEuMDAwMDAwLDE3OC43MDAwMTIgMzAxLjAwMDAwMCwxODEuNDAwMDI0IDMwMS4wMDAwMDAsMTg0LjU1MDAxOCAKCUMzMDAuMzM0MjI5LDE4NS42OTcyODEgMjk5LjI2NTgzOSwxODYuMjkzNTE4IDI5OS4wNjE3MDcsMTg3LjEwNjY1OSAKCUMyOTQuMjkwNzEwLDIwNi4xMTQ4MjIgMjg1LjY3OTcxOCwyMjMuMzM2NjcwIDI3My41Nzc2OTgsMjM4LjU3MzMwMyAKCUMyNTQuODMwMDkzLDI2Mi4xNzY3ODggMjMwLjY5MTIzOCwyNzcuMTI1MDYxIDIwMC41OTY4NDgsMjgyLjEwMTM3OSAKCUMxNjguMDc0NTI0LDI4Ny40NzkxNTYgMTM3LjMwNDA5MiwyODEuNDAzOTkyIDEwNy42MDQ3ODIsMjY4LjQzNjU1NCAKCUMxMTMuMTY3MzgxLDI2OS40NzcwMjAgMTE4LjU1MDY1OSwyNzAuODE5MzA1IDEyMy45MzM5MzcsMjcyLjE2MTU2MCAKeiIvPgo8cGF0aCBmaWxsPSIjNDk4MEI1IiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTI0LjM4MDk5NywyNzIuMTE0OTkwIAoJQzExOC41NTA2NTksMjcwLjgxOTMwNSAxMTMuMTY3MzgxLDI2OS40NzcwMjAgMTA3LjM5NTU1NCwyNjguMTYxNzc0IAoJQzgwLjAwODE2MywyNTkuMDQzNjEwIDYwLjI4ODk4NiwyNDAuODMwNDkwIDQ1LjI2MTkyNSwyMTcuMzU2OTQ5IAoJQzM1Ljg0ODQ5OSwyMDIuNjUyMzkwIDMwLjM0MjEyOSwxODYuMzQ1MTY5IDI3Ljg1MzE0NiwxNjguODYwMTg0IAoJQzIzLjgwMzM2NCwxNDAuNDEwNjYwIDI4LjUyODU0MywxMTMuNjg0MzY0IDQyLjE5NjQ5OSw4OC42MjE1NTIgCglDNTMuNjA2NjEzLDY3LjY5ODkxNCA2OS42MTQ0NTYsNTAuOTg3NjU2IDkwLjgwNjM1MSwzOS43NTA2MTggCglDOTcuOTYwMzA0LDM1Ljk1NzIyNiAxMDUuNjY5MzgwLDMzLjIxMDczOSAxMTMuODI1MDQzLDMwLjEwNDYwMSAKCUMxMjAuMzE2NDIyLDM1LjU5ODAyNiAxMjcuMDk0ODEwLDQwLjI1NTkyNCAxMzEuNjQ4NTYwLDQ2LjUyODc3OCAKCUMxMzcuMzMzOTY5LDU0LjM2MDQ5MyAxNDEuMTg3NzU5LDYzLjUyMTg0NyAxNDUuODY5NzgxLDcyLjUwODg5NiAKCUMxNDUuODg1OTEwLDczLjk3NzI4NyAxNDUuODY0NTYzLDc1LjA0NTkyMSAxNDUuNTIwNTA4LDc2LjIyODUzMSAKCUMxMzQuNzY2NjQ3LDgwLjU2MjI2MyAxMjQuODkwNzA5LDg1LjY3NDQzOCAxMTYuNjcwODgzLDk0LjA4Mjk0NyAKCUMxMTIuNzY3ODE1LDk4LjEyNzU0MSAxMDkuMTU3Mjg4LDEwMi4wMDQ3MDcgMTA1LjUzNTI0OCwxMDUuODcxMDg2IAoJQzEwMi42MjkzNDEsMTA4Ljk3MzAyMiAxMDMuMTIyMjc2LDExMS40MDMxMzcgMTA3LjE3NjI4NSwxMTMuNDM4MDk1IAoJQzExMS42NDYwODAsMTE1LjQyMzc2NyAxMTUuODkwMDQ1LDExNy4xNjc4NTQgMTIwLjEzNDAxMCwxMTguOTExOTQyIAoJQzEyMS4yNTQxOTYsMTE5LjEwNDE4NyAxMjIuMzc0MzgyLDExOS4yOTY0MzIgMTIzLjg2MzczOSwxMTkuNTUyMDQ4IAoJQzEyNi4wOTQzNjgsMTE1LjEzMjk1MCAxMjkuNjQyMDQ0LDExMi40ODk5MjIgMTM1LjY4MDI1MiwxMTQuNTcxMTY3IAoJQzEzNS43Njc0NTYsMTE1LjU1NTEyMiAxMzUuODkwMDkxLDExNi45Mzg4NDMgMTM2LjAzODg2NCwxMTguNjE3NDg1IAoJQzEzNC45Njk3NDIsMTE4Ljc3MTg2NiAxMzQuMTc0MzkzLDExOS4wNTQwNzAgMTMzLjQyMTk5NywxMTguOTY2NjQ0IAoJQzEzMC4wMTU0NDIsMTE4LjU3MDgwOCAxMjkuMDM0OTEyLDEyMC41NzU0NzAgMTI5LjAzMzU4NSwxMjMuNDAwOTAyIAoJQzEyOS4wMzIzMDMsMTI2LjExNTY2MiAxMjkuNzQwMzExLDEyOC4xODM0NzIgMTMzLjIyNTg0NSwxMjguMTAwODE1IAoJQzEzNC40MzQ3ODQsMTI4LjA3MjE1OSAxMzUuNjcxMjk1LDEyOS4yMDU5MzMgMTM2Ljg5NTIwMywxMjkuODA4Nzc3IAoJQzEzNi4xMjUzMDUsMTMxLjE2MzIyMyAxMzUuMzU1NDIzLDEzMi41MTc2NzAgMTM0LjU0NDg2MSwxMzMuOTQzNjY1IAoJQzEzNC41NDQ4NjEsMTM0Ljk2MDMxMiAxMzQuOTc0ODU0LDEzNi42MzYxMzkgMTM0LjM3MDg4MCwxMzcuNzUyNjcwIAoJQzEzNC4wNDkxOTQsMTM4LjM0NzM4MiAxMzEuOTM1MzY0LDEzOC4wNjkwNjEgMTMwLjYzNjc0OSwxMzguMDE5NTAxIAoJQzEyNy42NjA1MDAsMTM3LjkwNTg1MyAxMjQuMTg4MzAxLDEzOC44OTk1OTcgMTIyLjYyMjI3NiwxMzUuMDk2MjgzIAoJQzEyMS45MDY2OTMsMTMzLjM1ODQxNCAxMjEuMDk2Njg3LDEzMS40NzkzODUgMTIxLjEwMzg4MiwxMjkuNjY3NDUwIAoJQzEyMS4xMTM4OTIsMTI3LjE0MjgxNSAxMjAuNDI2MTcwLDEyNS41ODM2NDkgMTE3LjEzOTUyNiwxMjQuOTQ1NTQxIAoJQzEwOS45MzUxNDMsMTIyLjc0Nzc5NSAxMDMuNDc5MDczLDEyMC42Njg1NzkgOTYuNzg0ODY2LDExOC4zODY2NTAgCglDODguNzk4MzQwLDExNC40NTI4NTAgOTAuOTg1MTQ2LDEwOC4zNzY5NDUgOTMuNjA2ODY1LDEwMi4xOTg0MDIgCglDODQuNjgyNDA0LDExMS40MzQxNjYgODUuMjEzNzY4LDExNy4wMDcyNzggOTQuNjUzNjk0LDEyMi40NTY1MTIgCglDOTMuOTY5NjM1LDEyNC40OTkyNjAgOTMuMzY4MjcxLDEyNi4yMDk4NDYgOTIuNjg0OTc1LDEyNy44ODcwNTQgCglDODguMTAxNTQwLDEzOS4xMzczNDQgODUuNDQ2OTM4LDE1MC43OTk0NTQgODUuMTA4ODcxLDE2My40MjgzNzUgCglDODUuMzg2NjEyLDE4NS45OTY3OTYgOTEuNDg4MTA2LDIwNi4yMTUzOTMgMTA0Ljc5NTM4MCwyMjQuMzMxNTczIAoJQzEwNC44Njg4ODksMjI0LjU1NTg0NyAxMDUuMDI2NDQzLDIyNS4wMDA2NTYgMTA0Ljk5MzE5NSwyMjUuMjQxMTUwIAoJQzEwNC45NTk5NTMsMjI1LjQ4MTY1OSAxMDQuOTA3MjY1LDIyNS45NjQzODYgMTA0LjcyNTk0NSwyMjYuMjkzNDU3IAoJQzEwMy42MjQwMzksMjMzLjE4ODcwNSAxMDkuODU1MDE5LDI0Ni4wMTE4NDEgMTE0LjYwMjQwMiwyNDguNjcwODIyIAoJQzExMy4xNDUzNzAsMjQyLjU0Njk4MiAxMTEuNTI4MzM2LDIzNS43NTA2NTYgMTEwLjEwOTM2NywyMjguNjc1MTEwIAoJQzExMS44OTg1MjksMjI3LjI2MjQ2NiAxMTMuMzY4MTg3LDIyNS44NzE2NzQgMTE1LjEwNjk3OSwyMjUuMDUxMzAwIAoJQzExOC4zMzg5NTksMjIzLjUyNjQyOCAxMjEuNzI3ODY3LDIyMi4zMzQxODMgMTI1LjQwMjkxNiwyMjAuOTg4NDY0IAoJQzEyNi44NDI3ODksMjIwLjYyNDM3NCAxMjcuOTMxMTgzLDIyMC4yNzUyMzggMTI5LjAxOTU3NywyMTkuOTI2MTE3IAoJQzEzMi43NjU1MTgsMjE5LjU3NTYyMyAxMzYuNTExNDU5LDIxOS4yMjUxNDMgMTQwLjIwNjA4NSwyMTguODc5NDU2IAoJQzE0MC43NjY0NzksMjE2LjA5NjU3MyAxNDAuNzkzMzY1LDIxMy4xMzI2OTAgMTQxLjk4MTAxOCwyMTAuNzQ2NjEzIAoJQzE0My42NDk1MjEsMjA3LjM5NDQ1NSAxNTAuODU4MDQ3LDIwNS4wMTkxMDQgMTUzLjY4MzA5MCwyMDcuMzA3ODE2IAoJQzE1NS42NzE2MTYsMjA4LjkxODgwOCAxNTYuMTU5NzQ0LDIxMi42MTI3NzggMTU2Ljc0NTk1NiwyMTUuNDkzMDU3IAoJQzE1Ni44NDIwNTYsMjE1Ljk2NTI0MCAxNTMuNzg4MTQ3LDIxNi44MTUyOTIgMTUyLjUzNDk1OCwyMTcuODkyMDU5IAoJQzE1MC45NzI4MzksMjE5LjIzNDMxNCAxNDkuMzk5NzUwLDIyMC44MjE2MDkgMTQ4LjU1NTI1MiwyMjIuNjM5Mzg5IAoJQzE0OC4wODg3NjAsMjIzLjY0MzU1NSAxNDkuMTAyNzUzLDIyNS4zMzU0OTUgMTQ5LjQ4NDUxMiwyMjYuODU3NTc0IAoJQzE1MS4xNTg1ODUsMjI2Ljk1NDA3MSAxNTIuNzgzNTU0LDIyNy4wNDc3MjkgMTU0LjY5MDYxMywyMjcuMTU3NjM5IAoJQzE1NC42OTA2MTMsMjI4LjcxODUyMSAxNTQuNjkwNjEzLDIzMC4xMDkwMzkgMTU0LjY5MDYxMywyMzEuNzYzMzY3IAoJQzE0OS4wMjA0NDcsMjMyLjY3MjU3NyAxNDUuMDk4Njk0LDIzMC43MDUxMDkgMTQzLjA3NDgyOSwyMjUuMTc0Nzc0IAoJQzEzOS44Njc0NzcsMjI1LjgyMDcwOSAxMzYuODk5NDYwLDIyNi40MTg0NDIgMTMzLjE3MjMwMiwyMjcuMTE5NzUxIAoJQzEyOS40OTA4NzUsMjI4LjU5NTQ5MCAxMjYuMzc5Mzc5LDIyOS42OTA1NTIgMTIzLjc0NzQwNiwyMzEuNDg3ODM5IAoJQzEyMi44MDY4MDEsMjMyLjEzMDE0MiAxMjMuMDI2Mjc2LDIzNC40NzEyODMgMTIyLjgzMjQ0MywyMzYuMzgyOTY1IAoJQzEyNC4yMTg5NDgsMjM5LjQ5MjY2MSAxMjUuNDg5MjY1LDI0Mi4yNTY0MDkgMTI2Ljg3MTM5OSwyNDUuMzUzNTQ2IAoJQzEzNC4xMzAzNTYsMjQ5Ljg5ODMxNSAxNDEuMjc3NTEyLDI1NC4xMDk2NTAgMTQ4LjczOTE2NiwyNTguNTE2Mzg4IAoJQzE2Mi43MTQ4NDQsMjY0LjU0OTcxMyAxNzYuODY5NDE1LDI2Ny40Nzg3NjAgMTkxLjcwNTAzMiwyNjUuMTQ2MjEwIAoJQzIwMC4xODU5MTMsMjYzLjgxMjc0NCAyMDguNTY3MjkxLDI2MS44NDY0MDUgMjE2Ljk5MzQ2OSwyNjAuMTY1MDM5IAoJQzIwOS41NzU5MjgsMjYzLjMxMDk3NCAyMDIuNDE1MDU0LDI2Ny41ODY4ODQgMTk0LjY4MTkxNSwyNjkuMzQzMjkyIAoJQzE4Mi40NzAyOTEsMjcyLjExNjgyMSAxNjkuOTIwNzYxLDI3NC4wMTkxMDQgMTU3LjQyNjAyNSwyNzQuNzIyMTk4IAoJQzE0OC40NTgzODksMjc1LjIyNjg5OCAxMzkuMzQ4NTcyLDI3My4xNTI5NTQgMTMwLjI5NzcyOSwyNzIuMjc1NDIxIAoJQzEyOC40ODQ4NjMsMjcyLjA5OTY0MCAxMjYuNjUxODEwLDI3Mi4xMzE5ODkgMTI0LjM4MDk5NywyNzIuMTE0OTkwIAp6Ii8+CjxwYXRoIGZpbGw9IiM2MzlDNEUiIG9wYWNpdHk9IjEuMDAwMDAwIiBzdHJva2U9Im5vbmUiIAoJZD0iCk0xNDUuODQzMjMxLDc2LjExNDU0OCAKCUMxNDUuODY0NTYzLDc1LjA0NTkyMSAxNDUuODg1OTEwLDczLjk3NzI4NyAxNDUuOTE0MDMyLDcyLjA0Mzg2OSAKCUMxNDYuMDA0NDI1LDY4LjExODE1NiAxNDYuMDg4MDQzLDY1LjA1NzI0MyAxNDYuMTcxNjQ2LDYxLjk5NjMzMCAKCUMxNDcuMzA0NTM1LDYxLjA2NTIzNSAxNDguNTQ2ODE0LDYwLjIzODQ0MSAxNDkuNTUxMzE1LDU5LjE4NDkzNyAKCUMxNTMuODU3ODE5LDU0LjY2ODMzMSAxNjEuMDU1MTMwLDU1LjQwODg3NSAxNjMuNTUyMDAyLDYxLjE0OTkyOSAKCUMxNjYuNTA0NTYyLDY3LjkzODcyMSAxNzEuODg2MTA4LDcwLjg4Nzk0NyAxNzguNTg1NDgwLDcxLjg5NDI0MSAKCUMxOTYuNTM3OTMzLDc0LjU5MDg0MyAyMTQuMzQyNDg0LDcyLjc0NzUxMyAyMzIuMDgwNTgyLDY5LjY5MzMzNiAKCUMyMzMuNzE0MTI3LDY5LjQxMjA2NCAyMzUuMzY1MTQzLDY5LjIzMjI4NSAyMzcuNDIxNjAwLDY4Ljk5MDI5NSAKCUMyMzYuMjI1NjAxLDc0LjMzNDc2MyAyMzEuODg0NjQ0LDc2LjI4NjM2OSAyMjcuMDE5MjI2LDc2LjkyNTA1NiAKCUMyMDQuOTEwMjk0LDc5LjgyNzMwMSAxODMuMjY1Nzc4LDg0LjY4Nzg1MSAxNjIuMTgwMTQ1LDkxLjkzNjUzOSAKCUMxNTYuMDA3MTcyLDk0LjA1ODY0NyAxNDkuOTgwMDcyLDk2LjYwNTExMCAxNDMuNTAyOTYwLDk4LjU4MzA5OSAKCUMxNDMuNDI1NTk4LDk1LjgwOTEzNSAxNDMuNzMxMzY5LDkzLjQwOTE0MiAxNDQuMjU3MjAyLDkwLjY4MDE1MyAKCUMxNDQuOTMyNjAyLDg1LjYwNTYyMSAxNDUuMzg3OTI0LDgwLjg2MDA4NSAxNDUuODQzMjMxLDc2LjExNDU0OCAKeiIvPgo8cGF0aCBmaWxsPSIjM0E2MjgzIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTA0LjcyMTg2MywyMjQuMTA3MzE1IAoJQzkxLjQ4ODEwNiwyMDYuMjE1MzkzIDg1LjM4NjYxMiwxODUuOTk2Nzk2IDg1LjQxNTM2NywxNjMuMjkyOTY5IAoJQzg2LjgwODgwNywxNjAuOTEyNDMwIDg3Ljk1MDA2NiwxNTkuMTcyMjI2IDg4LjkwNDE5MCwxNTcuMzM0ODI0IAoJQzkyLjQ2NTQwMSwxNTAuNDc2ODA3IDk1LjYwMzMyNSwxNDMuMzY1NjQ2IDk5LjYyMjg3OSwxMzYuNzkxMzk3IAoJQzEwMi4wNjI4MjgsMTMyLjgwMDY5MCAxMDUuODMwMDQwLDEyOS42MjE0NzUgMTA5LjQzODYwNiwxMjYuMDY4NzcxIAoJQzExMi4yMDMyMDEsMTI2LjA1MDE1NiAxMTQuNTMwMTkwLDEyNi4wNDA0NzQgMTE2Ljg1NzE3OCwxMjYuMDMwNzkyIAoJQzExNi40NTc0OTcsMTI3LjI0Njg5NSAxMTYuMDU3ODA4LDEyOC40NjI5OTcgMTE1LjAyODEzNywxMjkuOTA1NDg3IAoJQzExMy4wODIwMzksMTMwLjc5MDA3MCAxMTEuNTUxODY1LDEzMS4yMDQwNzEgMTEwLjQ4MTM2OSwxMzIuMTQyNDQxIAoJQzg4LjYwODE1NCwxNTEuMzE2MTAxIDg0LjU1NTMzNiwxODQuMzg2OTc4IDEwMy4yMTUxODcsMjA3LjY3OTk3NyAKCUMxMDYuOTE4NTk0LDIxMi4zMDI5MDIgMTExLjA1OTczMSwyMTYuNTc1MTk1IDExNC42NTkwMjcsMjIxLjE0MzczOCAKCUMxMTEuNTMwNjQ3LDIyMi4xODE3MTcgMTA4Ljc0MjI0OSwyMjMuMDg1MTI5IDEwNS42NDU3ODIsMjI0LjAxNzUxNyAKCUMxMDUuMTMyNDM5LDIyNC4wNjY3NzIgMTA0LjkyNzE1NSwyMjQuMDg3MDM2IDEwNC43MjE4NjMsMjI0LjEwNzMxNSAKeiIvPgo8cGF0aCBmaWxsPSIjM0Q2NzhBIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTI4Ljg3OTcwMCwyMTkuNjA2ODEyIAoJQzEyNy45MzExODMsMjIwLjI3NTIzOCAxMjYuODQyNzg5LDIyMC42MjQzNzQgMTI1LjE0MzI1NywyMjAuOTczNjMzIAoJQzEyNC4zNTkzMTQsMjIwLjk2MDk2OCAxMjQuMTg2NTE2LDIyMC45NDgxNTEgMTIzLjg5NTUyMywyMjAuNjE4MDQyIAoJQzEyMi4zNzQyMjksMjE4Ljk0OTgyOSAxMjEuMTQyNjMyLDIxNy4zMzc3MDggMTE5LjU0MjM2NiwyMTYuMjg3MTcwIAoJQzk1LjE4MDg0MCwyMDAuMjkzODg0IDg4Ljk5NzUyOCwxNjcuNjQ4MjI0IDEwNi4xMDE1NTUsMTQ0LjA2NDAxMSAKCUMxMDcuODYzOTYwLDE0MS42MzM4ODEgMTEwLjc1Njk5NiwxNDAuMDIzNzI3IDExMy4xMjUzOTcsMTM4LjAzMzA4MSAKCUMxMTIuNzM4NTE4LDE0Mi4wNzA0NTAgMTEyLjM1MTYzOSwxNDYuMTA3ODE5IDExMS41ODY1OTQsMTUwLjY5ODMwMyAKCUMxMDkuOTI2NzY1LDE1Mi43MDI1MTUgMTA4LjIxOTMwNywxNTMuOTUzODczIDEwNy40MzAyNjcsMTU1LjYzNjAxNyAKCUMxMDAuNjQxNjYzLDE3MC4xMDg2ODggMTAyLjA5OTQ5NSwxODQuMjc5NjYzIDExMC42MTcwMDQsMTk3LjM3NTAwMCAKCUMxMTMuNjIwOTQ5LDIwMS45OTM0NTQgMTE4Ljg4NDk3OSwyMDUuMTQxODkxIDEyMy4xMTcxMTEsMjA4Ljk2MTUwMiAKCUMxMjQuOTkxMzQxLDIxMi40MDM1MDMgMTI2Ljg2NTU3OCwyMTUuODQ1NDkwIDEyOC44Nzk3MDAsMjE5LjYwNjgxMiAKeiIvPgo8cGF0aCBmaWxsPSIjM0I2NDg2IiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTEzLjQyMjkxMywxMzcuNzk5NTAwIAoJQzExMC43NTY5OTYsMTQwLjAyMzcyNyAxMDcuODYzOTYwLDE0MS42MzM4ODEgMTA2LjEwMTU1NSwxNDQuMDY0MDExIAoJQzg4Ljk5NzUyOCwxNjcuNjQ4MjI0IDk1LjE4MDg0MCwyMDAuMjkzODg0IDExOS41NDIzNjYsMjE2LjI4NzE3MCAKCUMxMjEuMTQyNjMyLDIxNy4zMzc3MDggMTIyLjM3NDIyOSwyMTguOTQ5ODI5IDEyMy40NDQyMjksMjIwLjYzMzMwMSAKCUMxMjAuNDA3MTA0LDIyMC45ODAzMDEgMTE3LjcwMzA1NiwyMjAuOTk0NzUxIDExNC45OTkwMDgsMjIxLjAwOTE4NiAKCUMxMTEuMDU5NzMxLDIxNi41NzUxOTUgMTA2LjkxODU5NCwyMTIuMzAyOTAyIDEwMy4yMTUxODcsMjA3LjY3OTk3NyAKCUM4NC41NTUzMzYsMTg0LjM4Njk3OCA4OC42MDgxNTQsMTUxLjMxNjEwMSAxMTAuNDgxMzY5LDEzMi4xNDI0NDEgCglDMTExLjU1MTg2NSwxMzEuMjA0MDcxIDExMy4wODIwMzksMTMwLjc5MDA3MCAxMTQuNzU4MzQ3LDEzMC4wODY1NDggCglDMTE0LjY1MjUwNCwxMzIuNTQ5NDU0IDExNC4xODY0NjIsMTM1LjA1NzY5MyAxMTMuNDIyOTEzLDEzNy43OTk1MDAgCnoiLz4KPHBhdGggZmlsbD0iIzNGNkI5MSIgb3BhY2l0eT0iMS4wMDAwMDAiIHN0cm9rZT0ibm9uZSIgCglkPSIKTTEyMy4wNDk2MDYsMjA4LjU4OTI3OSAKCUMxMTguODg0OTc5LDIwNS4xNDE4OTEgMTEzLjYyMDk0OSwyMDEuOTkzNDU0IDExMC42MTcwMDQsMTk3LjM3NTAwMCAKCUMxMDIuMDk5NDk1LDE4NC4yNzk2NjMgMTAwLjY0MTY2MywxNzAuMTA4Njg4IDEwNy40MzAyNjcsMTU1LjYzNjAxNyAKCUMxMDguMjE5MzA3LDE1My45NTM4NzMgMTA5LjkyNjc2NSwxNTIuNzAyNTE1IDExMS41MjE2MDYsMTUxLjEzMDU1NCAKCUMxMTEuNTQ3NDMyLDE3MC44NTg4NTYgMTE1LjQzMDc3OSwxODkuODk1MzI1IDEyMy4wNDk2MDYsMjA4LjU4OTI3OSAKeiIvPgo8cGF0aCBmaWxsPSIjNjM5QzRFIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTkzLjA0OTIyNSwyMS45MjI5NjYgCglDMTkzLjkxNTE2MSwyNC4yMTMwNDkgMTk1LjA0ODY0NSwyNi40OTI1OTIgMTk1LjUyOTI5NywyOC45MDIzNDggCglDMTk2LjQ0NTYzMywzMy40OTYzNDYgMTk2LjExODc1OSwzNy44NzE4MDcgMTkxLjI5NjQ0OCw0MC40ODY3NzQgCglDMTkyLjI0NDQ3NiwzNi4yOTg3MzMgMTkxLjQ0OTEyNywzMi43MzMzNDUgMTg4LjMwNTYxOCwzMC4xOTI1MDUgCglDMTg1LjEwMzk3MywyNy42MDQ2NzcgMTgxLjU4NDU0OSwyNy41MTg1MDkgMTc3Ljk1MjU0NSwyOS45NzcxNjAgCglDMTcyLjMyNjY3NSwzMy43ODU1NTcgMTczLjA5NzM5NywzOS44NTQ2ODcgMTgwLjAyMDc5OCw0NC45Mjg2NzcgCglDMTc0LjgyODAxOCw0Ni4xOTMzNDQgMTcyLjMxMzg1OCw0Mi4zMTY3NDYgMTcwLjA3MTc0NywzOS4wNTkxMTYgCglDMTY3LjE2ODcxNiwzNC44NDExOTQgMTY3LjA4MTc3MiwyOS45MTQxMjUgMTY5LjU1OTg0NSwyNS4zMTQyMzYgCglDMTcyLjY4MDkyMywxOS41MjA4MDMgMTc3Ljg2Mjk2MSwxNy41MDA1NzQgMTg0LjY1MjY3OSwxNy45NzQ1NjQgCglDMTg3LjIwMDA1OCwxOC45MzIwNTMgMTg5LjMwNjM1MSwxOS44OTI4ODMgMTkxLjkxMDc5NywyMS4xNTE5MjQgCglDMTkyLjY2NDgxMCwyMS42MTgzNTEgMTkyLjkwMTA5MywyMS44MTA2MjMgMTkzLjExNzc5OCwyMi4wMjY5NDkgCglDMTkzLjExNzc5OCwyMi4wMjY5NDkgMTkzLjAyMTk3MywyMS45NzEyMzAgMTkzLjA0OTIyNSwyMS45MjI5NjYgCnoiLz4KPHBhdGggZmlsbD0iIzM1NTk3NSIgb3BhY2l0eT0iMS4wMDAwMDAiIHN0cm9rZT0ibm9uZSIgCglkPSIKTTE0NC4wMzcxNDAsOTEuMDA5MTQ4IAoJQzE0My43MzEzNjksOTMuNDA5MTQyIDE0My40MjU1OTgsOTUuODA5MTM1IDE0My4xMzkwNjksOTguNjA4NzA0IAoJQzE0MC43MTk5NzEsOTkuOTkxNTg1IDEzOC4yODE2MDEsMTAwLjk3NDkwNyAxMzUuMDQ2NTU1LDEwMS45OTU3MjggCglDMTI0LjA3ODk4NywxMDMuMTM1MDEwIDExNC42MjgyMjcsMTA1Ljk5Nzg3MSAxMDYuOTUwNDYyLDExMy4xOTY1MDMgCglDMTAzLjEyMjI3NiwxMTEuNDAzMTM3IDEwMi42MjkzNDEsMTA4Ljk3MzAyMiAxMDUuNTM1MjQ4LDEwNS44NzEwODYgCglDMTA5LjE1NzI4OCwxMDIuMDA0NzA3IDExMi43Njc4MTUsOTguMTI3NTQxIDExNi44NTgzMzAsOTQuMzQ4MDA3IAoJQzExOS42NDI5NzUsOTQuNDIwMzAzIDEyMS45OTIwNDMsOTQuNjY1MDE2IDEyNC4yNTQ4MDcsOTQuMzI4ODU3IAoJQzEzMC44NjczNzEsOTMuMzQ2NDk3IDEzNy40NDU1MjYsOTIuMTMyNDE2IDE0NC4wMzcxNDAsOTEuMDA5MTQ4IAp6Ii8+CjxwYXRoIGZpbGw9IiMzMjU0NkQiIG9wYWNpdHk9IjEuMDAwMDAwIiBzdHJva2U9Im5vbmUiIAoJZD0iCk0yMTcuMzA3NDk1LDI1OS45OTY4ODcgCglDMjA4LjU2NzI5MSwyNjEuODQ2NDA1IDIwMC4xODU5MTMsMjYzLjgxMjc0NCAxOTEuNzA1MDMyLDI2NS4xNDYyMTAgCglDMTc2Ljg2OTQxNSwyNjcuNDc4NzYwIDE2Mi43MTQ4NDQsMjY0LjU0OTcxMyAxNDkuMTUxMDMxLDI1OC4zNDQ0MjEgCglDMTUzLjIwMDc0NSwyNTYuOTY4OTk0IDE1Ny4xNTMxMDcsMjU1Ljk2MDk2OCAxNjEuMTA1NDY5LDI1NC45NTI5NDIgCglDMTY4Ljk3NDQ3MiwyNTguMzA0MzIxIDE3Ni43OTc2ODQsMjYxLjMzMzk1NCAxODUuNTM5ODEwLDI2Mi4zMDA5MzQgCglDMTk1LjczNTgyNSwyNjMuNDI4NzExIDIwNS4xNjUwMjQsMjYxLjI5NzI3MiAyMTQuNDkyNDYyLDI1OC4wODQwNzYgCglDMjE5LjkyNjUxNCwyNTYuMjEyMDk3IDIyNS4wNTAwOTUsMjUzLjQzODkwNCAyMzAuNjc5OTQ3LDI1MS4wNTAwMTggCglDMjI2LjU3MTUzMywyNTMuOTYyMTQzIDIyMi4wOTY1MjcsMjU2Ljg5NTQ0NyAyMTcuMzA3NDk1LDI1OS45OTY4ODcgCnoiLz4KPHBhdGggZmlsbD0iIzM1NTk3NSIgb3BhY2l0eT0iMS4wMDAwMDAiIHN0cm9rZT0ibm9uZSIgCglkPSIKTTE2MC45MDI0MDUsMjU0LjY3NjgxOSAKCUMxNTcuMTUzMTA3LDI1NS45NjA5NjggMTUzLjIwMDc0NSwyNTYuOTY4OTk0IDE0OC44MzY1MTcsMjU4LjE0ODk4NyAKCUMxNDEuMjc3NTEyLDI1NC4xMDk2NTAgMTM0LjEzMDM1NiwyNDkuODk4MzE1IDEyNy4zMzYwMTQsMjQ1LjM1MjA1MSAKCUMxMjkuNDgzNjU4LDI0NS4xMjMxMjMgMTMxLjI3NzQwNSwyNDUuMjU1NTM5IDEzMy4wNzM1NDcsMjQ1LjMzMDEwOSAKCUMxMzguNDIwNDQxLDI0NS41NTIxMzkgMTQzLjc2ODI4MCwyNDUuNzUxNDM0IDE0OS4xMTU3MzgsMjQ1Ljk1OTYyNSAKCUMxNTIuOTc2OTQ0LDI0OC43NzMzMTUgMTU2LjgzODE1MCwyNTEuNTg3MDA2IDE2MC45MDI0MDUsMjU0LjY3NjgxOSAKeiIvPgo8cGF0aCBmaWxsPSIjMzg1RDdCIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTA3LjE3NjI4NSwxMTMuNDM4MDk1IAoJQzExNC42MjgyMjcsMTA1Ljk5Nzg3MSAxMjQuMDc4OTg3LDEwMy4xMzUwMTAgMTM0LjY4MzIxMiwxMDIuMDM1NzUxIAoJQzEzMC4xODk2ODIsMTA3LjQ0ODcyMyAxMjUuMjYyODEwLDExMi44NTkxNjkgMTIwLjIzNDk3OCwxMTguNTkwNzc1IAoJQzExNS44OTAwNDUsMTE3LjE2Nzg1NCAxMTEuNjQ2MDgwLDExNS40MjM3NjcgMTA3LjE3NjI4NSwxMTMuNDM4MDk1IAp6Ii8+CjxwYXRoIGZpbGw9IiMzODVEN0IiIG9wYWNpdHk9IjEuMDAwMDAwIiBzdHJva2U9Im5vbmUiIAoJZD0iCk0xNDguOTU0MzE1LDI0NS42NjU4OTQgCglDMTQzLjc2ODI4MCwyNDUuNzUxNDM0IDEzOC40MjA0NDEsMjQ1LjU1MjEzOSAxMzMuMDczNTQ3LDI0NS4zMzAxMDkgCglDMTMxLjI3NzQwNSwyNDUuMjU1NTM5IDEyOS40ODM2NTgsMjQ1LjEyMzEyMyAxMjcuMjI0MTk3LDI0NS4wMTg2NDYgCglDMTI1LjQ4OTI2NSwyNDIuMjU2NDA5IDEyNC4yMTg5NDgsMjM5LjQ5MjY2MSAxMjMuMjg4NDgzLDIzNi4zODAzMTAgCglDMTI5LjQ1NzY4NywyMzYuNjc0NjgzIDEzNS4yODcwNjQsMjM3LjMxNzY3MyAxNDEuMTE2NDI1LDIzNy45NjA2NjMgCglDMTQzLjY3NTI0NywyNDAuNDMxMTY4IDE0Ni4yMzQwNzAsMjQyLjkwMTY3MiAxNDguOTU0MzE1LDI0NS42NjU4OTQgCnoiLz4KPHBhdGggZmlsbD0iIzNBNjA4MSIgb3BhY2l0eT0iMS4wMDAwMDAiIHN0cm9rZT0ibm9uZSIgCglkPSIKTTE0MC45NTI2MDYsMjM3LjY2MDQxNiAKCUMxMzUuMjg3MDY0LDIzNy4zMTc2NzMgMTI5LjQ1NzY4NywyMzYuNjc0NjgzIDEyMy4xNzIyODcsMjM2LjAzNDMzMiAKCUMxMjMuMDI2Mjc2LDIzNC40NzEyODMgMTIyLjgwNjgwMSwyMzIuMTMwMTQyIDEyMy43NDc0MDYsMjMxLjQ4NzgzOSAKCUMxMjYuMzc5Mzc5LDIyOS42OTA1NTIgMTI5LjQ5MDg3NSwyMjguNTk1NDkwIDEzMi43NzI1MjIsMjI3LjE1NDk5OSAKCUMxMzUuNjg0MTg5LDIzMC41MTExNjkgMTM4LjIzNjQ5NiwyMzMuOTM1NjY5IDE0MC45NTI2MDYsMjM3LjY2MDQxNiAKeiIvPgo8cGF0aCBmaWxsPSIjMzI1MzZBIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTE2LjkzMDcxMCwxMjUuODA2NTExIAoJQzExNC41MzAxOTAsMTI2LjA0MDQ3NCAxMTIuMjAzMjAxLDEyNi4wNTAxNTYgMTA5LjAxNTQ3MiwxMjYuMDQ3NDA5IAoJQzEwNC4wNDI0MTIsMTI0LjY4NDAxMyA5OS45MzAwODQsMTIzLjMzMzA0NiA5NS45MzUyOTUsMTIxLjY0NDQxNyAKCUM5Ni4zNzYyMjgsMTIwLjQwMDk1NSA5Ni42OTk2MjMsMTE5LjQ5NTE2MyA5Ny4wMjMwMTAsMTE4LjU4OTM3MSAKCUMxMDMuNDc5MDczLDEyMC42Njg1NzkgMTA5LjkzNTE0MywxMjIuNzQ3Nzk1IDExNi43NDk1NTcsMTI0Ljk3NDM1MCAKCUMxMTcuMTA3OTEwLDEyNS4xMjE2OTYgMTE3LjAwNDI0MiwxMjUuNTgyMjMwIDExNi45MzA3MTAsMTI1LjgwNjUxMSAKeiIvPgo8cGF0aCBmaWxsPSIjMzI1NDZEIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMjMyLjY5NzcyMywyNTAuMTM4ODQwIAoJQzIzMi41MzA1MDIsMjUwLjQ3NzI0OSAyMzIuMDYxMDM1LDI1MC43ODUxODcgMjMxLjMwMjU1MSwyNTEuMDczNzc2IAoJQzIzMS40NzQxNjcsMjUwLjczOTA3NSAyMzEuOTM0ODE0LDI1MC40MjM3MjEgMjMyLjY5NzcyMywyNTAuMTM4ODQwIAp6Ii8+CjxwYXRoIGZpbGw9IiM2RUIyNTMiIG9wYWNpdHk9IjEuMDAwMDAwIiBzdHJva2U9Im5vbmUiIAoJZD0iCk0xOTMuMDMwMDYwLDIxLjc4MTgwOSAKCUMxOTIuOTAxMDkzLDIxLjgxMDYyMyAxOTIuNjY0ODEwLDIxLjYxODM1MSAxOTIuMjMwNzU5LDIxLjMwNjY1MCAKCUMxOTIuMzQ5MTUyLDIxLjI4NzY2NiAxOTIuNjQ1NzUyLDIxLjQxMjE2NyAxOTMuMDMwMDYwLDIxLjc4MTgwOSAKeiIvPgo8cGF0aCBmaWxsPSIjM0E2MTdGIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTQ2LjEyMjIwOCw2MS41NzAwMTUgCglDMTQ2LjA4ODA0Myw2NS4wNTcyNDMgMTQ2LjAwNDQyNSw2OC4xMTgxNTYgMTQ1Ljg3NjU3Miw3MS42NDQxMDQgCglDMTQxLjE4Nzc1OSw2My41MjE4NDcgMTM3LjMzMzk2OSw1NC4zNjA0OTMgMTMxLjY0ODU2MCw0Ni41Mjg3NzggCglDMTI3LjA5NDgxMCw0MC4yNTU5MjQgMTIwLjMxNjQyMiwzNS41OTgwMjYgMTE0LjIxMjkyOSwzMC4wNjYzNzIgCglDMTIxLjAyMjE5NCwyOC4wMTk0MzYgMTI4LjE0Mzg2MCwyNi4xMjk1MzggMTM1LjYxODQzOSwyNC4wNDIxODcgCglDMTM4LjU2OTU4MCwzMC44ODgyNjggMTQxLjU3ODU1MiwzNy44MTQ4NjkgMTQzLjYyODEyOCw0NS4wMTQ1OTEgCglDMTQ1LjEwNDk4MCw1MC4yMDI1MTUgMTQ1LjMwMzg2NCw1NS43NTQyNDIgMTQ2LjEyMjIwOCw2MS41NzAwMTUgCnoiLz4KPHBhdGggZmlsbD0iIzAwMDAwMCIgb3BhY2l0eT0iMS4wMDAwMDAiIHN0cm9rZT0ibm9uZSIgCglkPSIKTTE4MC40MzM2NTUsNDQuOTc5MzI0IAoJQzE3My4wOTczOTcsMzkuODU0Njg3IDE3Mi4zMjY2NzUsMzMuNzg1NTU3IDE3Ny45NTI1NDUsMjkuOTc3MTYwIAoJQzE4MS41ODQ1NDksMjcuNTE4NTA5IDE4NS4xMDM5NzMsMjcuNjA0Njc3IDE4OC4zMDU2MTgsMzAuMTkyNTA1IAoJQzE5MS40NDkxMjcsMzIuNzMzMzQ1IDE5Mi4yNDQ0NzYsMzYuMjk4NzMzIDE5MC45NjQwNjYsNDAuNTk4OTA3IAoJQzE4OC4xMDY2NDQsNDMuNjU3NjEyIDE4NS4wNTkwOTcsNDUuNzk1MDAyIDE4MC40MzM2NTUsNDQuOTc5MzI0IAp6Ii8+CjxwYXRoIGZpbGw9IiMzOTYwN0YiIG9wYWNpdHk9IjEuMDAwMDAwIiBzdHJva2U9Im5vbmUiIAoJZD0iCk05NS44MTc3NTcsMTIxLjk4MjA4NiAKCUM5OS45MzAwODQsMTIzLjMzMzA0NiAxMDQuMDQyNDEyLDEyNC42ODQwMTMgMTA4LjU3Nzg2NiwxMjYuMDU2MzQzIAoJQzEwNS44MzAwNDAsMTI5LjYyMTQ3NSAxMDIuMDYyODI4LDEzMi44MDA2OTAgOTkuNjIyODc5LDEzNi43OTEzOTcgCglDOTUuNjAzMzI1LDE0My4zNjU2NDYgOTIuNDY1NDAxLDE1MC40NzY4MDcgODguOTA0MTkwLDE1Ny4zMzQ4MjQgCglDODcuOTUwMDY2LDE1OS4xNzIyMjYgODYuODA4ODA3LDE2MC45MTI0MzAgODUuNDQ2OTc2LDE2Mi44MzI2NzIgCglDODUuNDQ2OTM4LDE1MC43OTk0NTQgODguMTAxNTQwLDEzOS4xMzczNDQgOTIuNjg0OTc1LDEyNy44ODcwNTQgCglDOTMuMzY4MjcxLDEyNi4yMDk4NDYgOTMuOTY5NjM1LDEyNC40OTkyNjAgOTQuOTM0MjA0LDEyMi40MjQzMzIgCglDOTUuNDQ1NTg3LDEyMi4wMjM3MjcgOTUuNjMxNjY4LDEyMi4wMDI5MDcgOTUuODE3NzU3LDEyMS45ODIwODYgCnoiLz4KPHBhdGggZmlsbD0iIzMzNTU2RSIgb3BhY2l0eT0iMS4wMDAwMDAiIHN0cm9rZT0ibm9uZSIgCglkPSIKTTE0NC4yNTcyMDIsOTAuNjgwMTUzIAoJQzEzNy40NDU1MjYsOTIuMTMyNDE2IDEzMC44NjczNzEsOTMuMzQ2NDk3IDEyNC4yNTQ4MDcsOTQuMzI4ODU3IAoJQzEyMS45OTIwNDMsOTQuNjY1MDE2IDExOS42NDI5NzUsOTQuNDIwMzAzIDExNy4xNDU4ODksOTQuMTc1OTE5IAoJQzEyNC44OTA3MDksODUuNjc0NDM4IDEzNC43NjY2NDcsODAuNTYyMjYzIDE0NS41MjA1MjMsNzYuMjI4NTMxIAoJQzE0NS4zODc5MjQsODAuODYwMDg1IDE0NC45MzI2MDIsODUuNjA1NjIxIDE0NC4yNTcyMDIsOTAuNjgwMTUzIAp6Ii8+CjxwYXRoIGZpbGw9IiMzQTYyODIiIG9wYWNpdHk9IjEuMDAwMDAwIiBzdHJva2U9Im5vbmUiIAoJZD0iCk0xMDkuOTExMzAxLDIyOC45NTQzMzAgCglDMTExLjUyODMzNiwyMzUuNzUwNjU2IDExMy4xNDUzNzAsMjQyLjU0Njk4MiAxMTQuNjAyNDAyLDI0OC42NzA4MjIgCglDMTA5Ljg1NTAxOSwyNDYuMDExODQxIDEwMy42MjQwMzksMjMzLjE4ODcwNSAxMDUuMDAyMTA2LDIyNi40NzYzNjQgCglDMTA2Ljk0MzQ4MSwyMjcuMjA0OTEwIDEwOC40MjczOTEsMjI4LjA3OTYyMCAxMDkuOTExMzAxLDIyOC45NTQzMzAgCnoiLz4KPHBhdGggZmlsbD0iIzNCNjM4MiIgb3BhY2l0eT0iMS4wMDAwMDAiIHN0cm9rZT0ibm9uZSIgCglkPSIKTTk1LjkzNTI5NSwxMjEuNjQ0NDA5IAoJQzk1LjYzMTY2OCwxMjIuMDAyOTA3IDk1LjQ0NTU4NywxMjIuMDIzNzI3IDk0Ljk3ODk4OSwxMjIuMDc2NzIxIAoJQzg1LjIxMzc2OCwxMTcuMDA3Mjc4IDg0LjY4MjQwNCwxMTEuNDM0MTY2IDkzLjYwNjg2NSwxMDIuMTk4NDAyIAoJQzkwLjk4NTE0NiwxMDguMzc2OTQ1IDg4Ljc5ODM0MCwxMTQuNDUyODUwIDk2Ljc4NDg2NiwxMTguMzg2NjUwIAoJQzk2LjY5OTYyMywxMTkuNDk1MTYzIDk2LjM3NjIyOCwxMjAuNDAwOTU1IDk1LjkzNTI5NSwxMjEuNjQ0NDA5IAp6Ii8+CjxwYXRoIGZpbGw9IiMzMjU1NkQiIG9wYWNpdHk9IjEuMDAwMDAwIiBzdHJva2U9Im5vbmUiIAoJZD0iCk0xMTAuMTA5MzY3LDIyOC42NzUxMTAgCglDMTA4LjQyNzM5MSwyMjguMDc5NjIwIDEwNi45NDM0ODEsMjI3LjIwNDkxMCAxMDUuMTgzNDI2LDIyNi4xNDcyNzggCglDMTA0LjkwNzI2NSwyMjUuOTY0Mzg2IDEwNC45NTk5NTMsMjI1LjQ4MTY1OSAxMDUuMTU2MjE5LDIyNS4wODAzNjggCglDMTA1LjU2MTU0NiwyMjQuNDU2MzkwIDEwNS43NjIwMDEsMjI0LjIyNjIxMiAxMDUuOTUzODQyLDIyMy45ODg1NDEgCglDMTA4Ljc0MjI0OSwyMjMuMDg1MTI5IDExMS41MzA2NDcsMjIyLjE4MTcxNyAxMTQuNjU5MDI3LDIyMS4xNDM3MzggCglDMTE3LjcwMzA1NiwyMjAuOTk0NzUxIDEyMC40MDcxMDQsMjIwLjk4MDMwMSAxMjMuNTYyNDM5LDIyMC45NTA2MDcgCglDMTI0LjE4NjUxNiwyMjAuOTQ4MTUxIDEyNC4zNTkzMTQsMjIwLjk2MDk2OCAxMjQuNzkxNzc5LDIyMC45ODg2MTcgCglDMTIxLjcyNzg2NywyMjIuMzM0MTgzIDExOC4zMzg5NTksMjIzLjUyNjQyOCAxMTUuMTA2OTc5LDIyNS4wNTEzMDAgCglDMTEzLjM2ODE4NywyMjUuODcxNjc0IDExMS44OTg1MjksMjI3LjI2MjQ2NiAxMTAuMTA5MzY3LDIyOC42NzUxMTAgCnoiLz4KPHBhdGggZmlsbD0iIzNBNjI4MiIgb3BhY2l0eT0iMS4wMDAwMDAiIHN0cm9rZT0ibm9uZSIgCglkPSIKTTEwNS42NDU3ODIsMjI0LjAxNzUxNyAKCUMxMDUuNzYyMDAxLDIyNC4yMjYyMTIgMTA1LjU2MTU0NiwyMjQuNDU2MzkwIDEwNS4xODk0NjgsMjI0LjgzOTg3NCAKCUMxMDUuMDI2NDQzLDIyNS4wMDA2NTYgMTA0Ljg2ODg4OSwyMjQuNTU1ODQ3IDEwNC43OTUzODAsMjI0LjMzMTU3MyAKCUMxMDQuOTI3MTU1LDIyNC4wODcwMzYgMTA1LjEzMjQzOSwyMjQuMDY2NzcyIDEwNS42NDU3ODIsMjI0LjAxNzUxNyAKeiIvPgo8L3N2Zz4=' alt="Run on Chameleon"/>
</a> First, you'll run the `reserve.ipynb` notebook to bring up a resource on Chameleon and configure it with the software needed to run this experiment. At the end of this notebook, you'll set up an SSH tunnel between your local device and a Jupyter notebook server that you just created on your Chameleon resource. Then, you'll open the notebook server in your local browser and run the sequence of notebooks you see there.
