## Deep Neural Nets: 33 years ago and 33 years from now

_Fraida Fund_

---

**Attribution**: This sequence of notebooks is adapted from the ICLR 2022 blog post ["Deep Neural Nets: 33 years ago and 33 years from now"](https://iclr-blog-track.github.io/2022/03/26/lecun1989/)  by Andrej Karpathy, and the associated [Github repository](https://github.com/karpathy/lecun1989-repro). 

---


In this sequence of experiments, you will reproduce a result from machine learning from 1989 - a paper that is possibly the earliest real-world application of a neural network trained end-to-end with backpropagation. (In earlier neural networks, some weights were actually hand-tuned!) You'll go a few steps further, though - after reproducing the results of the original paper, you'll get to use some modern 'tricks' to try and improve the performance of the model without changing its underlying infrastructure (i.e. no change in inference time!)

You can run this experiment on Google Colab: <a target="_blank" href="https://colab.research.google.com/github/teaching-on-testbeds/deep-nets-reproducing/blob/main/Deep_Neural_Nets_33_years_ago.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Or, you can use the Chameleon testbed: <img alt="Static Badge" src="https://img.shields.io/badge/-Run%20on%20Chameleon-green?logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACAAAAAfCAYAAACGVs%2BMAAAKdHpUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHjapZhZkiOxDUT%2FeQofgRu4HIdrhG%2Fg4%2FuBRWl6m7HHbkWrqksUCSITiWSb9a9%2FbvMPfoJN1kTJJdWULD%2BxxuobN8U%2BP%2B28OxvP%2B%2Fnx9yP%2B%2FvTcuG1fI5wNXMPzZ0l3%2FOu5e0%2FwXBp38mGiMu4H%2FfMHNd75y5eJbkhBI9L7eSeqd6Lgnw%2FcnaA927KplvxxC3091%2FnaYnl%2Bjb7F8jnsb39nsjeFdYL3K7hgeQ%2FhBhD0N5rQuEm8u1AZyCDuQyi8x1DuZCTkpzy9fyoRbQ01%2FjjoEyrvuy9o7Ru9%2BYpW9HdI%2BJLk9L7%2B%2BNw4%2BfJBeK%2FvP64cy73zn583edhm7Jfs6%2B%2Fes%2ByzZ3bRYiLV6W7qtcVzx7jOErp0MYSWbOZXmCKfV%2BVVWGdAhWmH7byGq86DxHbRTdfcdutchxuEGP0yPnPj%2FfDhPCwh%2B%2BpHUPyivtz2OdQwwdGHcWCPwb9jcWfZaoc5qxVWno6h3jGZ4yt%2F%2FTJ%2F%2B4W9tRScO7l8ACAu7zXZhKHI6TvDQOQWstae%2B%2FD6%2BqO4BhAUzbKWSCWx%2FZmii%2FulBOEAHRgoXJ8adHneCUgRSwvBuAACoOaCuORs9j47RyILADVCp4B8BwEn4idB%2BhhCApvidWm%2Bkt0Z6sXz2PAcMQMJoeIy2NTQACtGgT85FjjUJEgUkSRZilRpKaSYJKWUk4piyyFHkyWnnHPJNbcSSixSUsmllFpa9TUgmlJTzbXUWltjzcbMjW83BrTWfQ89djE99dxLr70N6DPikJFGHmXU0aafYaIfM808y6yzLbeg0opLVlp5lVVX21BtB7Pjlp123mXX3d6oXVi%2Fvf4CNXdR8wcpHZjfqPE059cUTuVEFDMA8yY6EM8KAYT2ipktLkavyClmtnqqQjxBimI2nSIGgnE5L9u9sDP%2BQVSR%2B79wMzl%2Bws3%2Fr8gZhe4vkfuO20%2BoTdW7cRB7qlCTagPVx%2BerNF%2BaNrtvV%2FPzB32RmF3bem4CXGGqlFfeiFkubYGIeHGyshvFT2%2BEB9bmoQOlVtnkQ%2Fhu9KGMvdZePsvIjt0wiMFUbRCmJu9I5FzTb%2FI1TNpxkfS5o9VofE9BnjsE5y%2Bu5tsHOycCb%2BjAbHNLlzJ8l7RBm8UzcpvqlLUywcU8Y9597pLNHirpbenWct7wFE712HpIPdE9RoJzObTWpm2Lh92TvDqyOOYenc2B1MQfDb5YZxykdJC%2FliaJSEOqB%2FPWYBksoYUMzT0Bt7gq0%2FVFVc25R6ZvuSlmCzQIK%2FUnQ2Sy%2F4Tuf7yaPueZROyGltAuBdum9FkFrk7iTVUzl%2BxmUPP1fFWgMxVSGlQlN8Euo3teyffcOrQey%2BUlh3ppzDkA%2BARKavEqjUlnpCRHzq6DNp%2FhFc4Qo1jt2pWCgW9obJks5oNQopIzZbEjmx938yVM%2F50A5gdm7Cx%2FIoBLJzXPZt9pMl%2FyliQqgjBgLOo21F6fusjgJjJaE7a04QUJadr9kZfMeAg54iyaQpZD7%2BCUykSaoKeNSmTVHaXkFCiru7sdZvqyO%2FN5V0JQO8eb4WK3HX%2FAvLTulGSRCE0rI61UNOoF9ZrSqrsuYTkI3NHW0olIq3VoXTu9f648QMvYXqByzW6zjURNVOLdfL%2F4A%2FfU%2Bt081dIpMy9qIVH5QuWvQ%2F4dU9k0tYUq1mZmaHlUiu8JGRGMv90M5FW2pXNVC8ZyGzBahpAhr7HHzQRastyvpJFxGDx9WsMWJD4g0N2mRrtYVGVwvboZkoJB76%2BUF0USSVHqJKqX7VghdUfvINpNtLvZ9mwXbVQHflhKfsaqLZNrv0n2yZ%2FwvfIxk88VwaTvyZAtKpd19C1Vi%2Fzk8OSzoEF5ZwP5%2ByOj%2FcFGy%2BlMJHowuVeEbKpG5%2B5IYdaK0hQvWp2qbZrNILd0T5ogeoeX7EfST%2FNW8s7gIUQv0NPhYqVUvFLyjRw7eOISIuBJY9wGsRCKCblafuYSZ0b0MrwiT2ErEEqAGDoOAKFZN9pcFy7gQy6MHG6UqSGONRubSFi0lj1LHABpKX6ggqo%2Biub3G1K2zM0ZEgQ9IrLRmWzTfsva6GyoXOwbj7qWbn4qCvA0aRq6ZvH0tedOzmalBqlImhYSBIToDdm0BaKia6vDxqHagQ3YOIhpAd%2Fup0R0FVlO4sFZEHV1Awi8m%2FVUwQPRpcmg5b%2FA1KzcfusNEJYDlZ8H7ovZhycKqX3D6bTJnimpuNXc4QV%2FG%2FXNy33nIttP9AXeUdumLHfKcKoG3kXpYain0bLy2JD4TSFfVy0K%2Bh240O9BTf3Qe8CplrkK7hvXdDqPGKSzKzJUHucaTTznrkN0uU8Q7UNfP9UsJGUgXqFHd4QQ8QpaMmZe9WzYqYA81NPIfqeO3dHIm2LnG9Xei0XBVBVokGyYutsO2ic514VlowG1bftLnDimtfHT9svDwFUMXAw0G3dYgXMLsJNVIgtfK6Wm9UB19kodpT1z2F1twUz50Cpq0S6PfPv31GqePk4sTcWdBMESzVJZ3WKYh72gwTSMSDd%2FUM8rnpTTQU%2FV8yaYOqN7UC1a%2FXFUOocpPQQ6F4Hj%2BQaQ4mckl4X0WFQAh%2BcX5g7jUmS1W%2FquzvRFs4x9VPARNvjQqAkSxMtVvCTP05FarRmlz1Hdkj5uHjWfwZy0ajloh%2FEp6u0zqyY17mPsiGfTfzA8D1FLu26gUra08RmXyT0V%2BjLWrPFkLExO9BEDPJ%2BCGm7VV%2BG4K7hvEXmkFUK87XHCqgj9NmFoAskq8HQt%2FIQeQRJtgUNhiO0IGR0HjwjL6vEt2zY14gYnfn04IuS1MK756WOHXv7k9o4ias2wx2wezwvhEUPIYqsKIBQdndMNHrB2TVrpjz%2BXwYkkqtpp57sSNRdnJvPWjbfo9666Qa1pdOR7uUHa60YUH%2FAbR8FfukNW8MBiqCEc0yIX2A4RbQRNOYgzsZp5oEVviibOni4UF%2FIKCpgncn%2BuY5Zt8BOkalq6qDusvkq%2Fcp3jW6OMt%2Fkq4ZDfgCTTJzm9NNOHcuF6CG07tg0VE5BK1ZWaaa0wfc6zKXwfHRtShd6cXffU0qMf5ps2cBTxv6oPTypbPak2qE2fOSeHw%2Bg7SaNAsQCmaUGqCcV6ID%2BKEefHOgvmBIFLSw8ldAiLjfNanVWWzFN2UzOo0oBtpdMib2q07A7udDIa12hYsKNKuFI8xcr9HPRUdznUKkVQfswCucHYZE50wbCAp10QUoJKXk9QfkZ8IK02YRLqPCTzBShjYdOpHS2GVI8xYkS3Rf%2FJ8qCEGbPf%2FdGX6%2BEYRgMSgkE%2FvVNhAxijlhR7gyNVRr4MSeCQL2N0yK6n0bDPv6ZWrAu7pw5Qq3VoN692qK1fZryHDVGTfrwAVhdNQUIaPQ1mkYspSGPcECxaaHHGqFqOhiniHEQX2VA%2F6ViwFTez5Qyhpzxiya9Fmujh7hgNRlFbZBH905OA6jJW2NCNkIepAjFYLhwvAW3exPMfiCch%2Fu6AbP7bk3SYzwkQ3Ca6IK8WLs%2FZVf%2Frd1xXS%2Bo4Qz7xhEK4OPv8srxqtX%2Bqu%2BNtONrqv6H%2FDeqLKYmeqcGlAAABhGlDQ1BJQ0MgcHJvZmlsZQAAeJx9kT1Iw0AcxV9TtSJVh3YQcchQnVoQFXHUKhShQqgVWnUwufQLmjQkKS6OgmvBwY%2FFqoOLs64OroIg%2BAHi7OCk6CIl%2Fi8ptIj14Lgf7%2B497t4BQr3MNKtrHNB020wl4mImuyoGXtGDEAYQQVRmljEnSUl0HF%2F38PH1LsazOp%2F7c%2FSrOYsBPpF4lhmmTbxBPL1pG5z3icOsKKvE58RRky5I%2FMh1xeM3zgWXBZ4ZNtOpeeIwsVhoY6WNWdHUiKeII6qmU76Q8VjlvMVZK1dZ8578hcGcvrLMdZojSGARS5AgQkEVJZRhI0arToqFFO3HO%2FiHXb9ELoVcJTByLKACDbLrB%2F%2BD391a%2BckJLykYB7pfHOdjFAjsAo2a43wfO07jBPA%2FA1d6y1%2BpAzOfpNdaWuQIGNwGLq5bmrIHXO4AQ0%2BGbMqu5Kcp5PPA%2Bxl9UxYI3QJ9a15vzX2cPgBp6ip5AxwcAmMFyl7v8O7e9t7%2BPdPs7wedeHK4FHRULwAADRppVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw%2FeHBhY2tldCBiZWdpbj0i77u%2FIiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8%2BCjx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDQuNC4wLUV4aXYyIj4KIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI%2BCiAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIgogICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgIHhtbG5zOkdJTVA9Imh0dHA6Ly93d3cuZ2ltcC5vcmcveG1wLyIKICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIgogICB4bXBNTTpEb2N1bWVudElEPSJnaW1wOmRvY2lkOmdpbXA6ZDFiYzRhZTItMDc0OC00ZTk5LTlmM2QtMTYyZjFkM2RkMTM5IgogICB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjI1ZDYxMzVmLTY3YzUtNDM3MS1hMTczLWI4MjlkMzRmMjAyNSIKICAgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOjA1MDZiOTQzLTg4MzUtNDY0YS04ZTQ0LTExZTg1MDQ4ODQ5OCIKICAgZGM6Rm9ybWF0PSJpbWFnZS9wbmciCiAgIEdJTVA6QVBJPSIyLjAiCiAgIEdJTVA6UGxhdGZvcm09IkxpbnV4IgogICBHSU1QOlRpbWVTdGFtcD0iMTcxODgwNzkzNDA2MjgxMSIKICAgR0lNUDpWZXJzaW9uPSIyLjEwLjMwIgogICB0aWZmOk9yaWVudGF0aW9uPSIxIgogICB4bXA6Q3JlYXRvclRvb2w9IkdJTVAgMi4xMCI%2BCiAgIDx4bXBNTTpIaXN0b3J5PgogICAgPHJkZjpTZXE%2BCiAgICAgPHJkZjpsaQogICAgICBzdEV2dDphY3Rpb249InNhdmVkIgogICAgICBzdEV2dDpjaGFuZ2VkPSIvIgogICAgICBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOmY4NjVmMzZiLWJlNDgtNDc4OS1iNzdlLTFiYzI1OWY1MzAzOCIKICAgICAgc3RFdnQ6c29mdHdhcmVBZ2VudD0iR2ltcCAyLjEwIChMaW51eCkiCiAgICAgIHN0RXZ0OndoZW49IjIwMjQtMDYtMTlUMTA6Mzg6NTQtMDQ6MDAiLz4KICAgIDwvcmRmOlNlcT4KICAgPC94bXBNTTpIaXN0b3J5PgogIDwvcmRmOkRlc2NyaXB0aW9uPgogPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgIAo8P3hwYWNrZXQgZW5kPSJ3Ij8%2B5Y3XMQAAAAZiS0dEAP8A%2FwD%2FoL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB%2BgGEw4mNv3VBSkAAAXeSURBVEjHtZd7jNRXFcc%2F5%2FfYnX0v8iiPpZSaGqtgbGx8YI2S1nYXO2OpQQuVxOyO8RFr01BECdEJQuyi0YANtGXHKBqMCavO4C4k1GzjoxIaqE3BIFTWuBYD7IPdmfnN%2FGbmd49%2F7ID7mn3QepP7z7n3nvM9557zvecKtzCePPqZHwJfBv4KdCkc2hfu7LsVXXJrAB6dh3IBWFASBaok%2FJHg%2B89vTpz8vwJY07qzCg0%2B9K41l7fX3zb4SQAUvMGCakC%2FXSEvV81zntob7ux9WwE0x7rvA75eyPR%2FKtt%2FqbqypsDqB88jAqaoZAaKPxD4hhOS46EG52MoOxB%2BtDfcqW8JQHOsa4XAs8DDN2QFbwjv2kVWP3iJylqvJDPHnEr5DnBIbHl3aetRYOO%2BcGfmlgA0x7paQA4DjRPXsgO9rFj9Go2LB2Zy40WUh%2FZFOs1Ui1a5Uy2xrg0CSUEbBWXiDDUuw087ZK4WCHyDKOXmAwLN5ew4Ze57DfDzcusAll2BCZaA9uEPB5gaxXYFsQRVUFU0AA102HLlwqwBNMe66oDDCpVlg6qG7NCbhOw3URk16KcNQAC8KvAX4FXgHHAuHk1m5hAB2QGsmMooYhHkPUb6XqPop1i4JA2QAhICvwVOxKPJkbmUtTP%2B3rvnA1%2BbbDtAMZh8luF%2FnUZNgG27Z2yH5wQOT%2BfhnAAAjwPVEzcFfho7VEfq8llEBLHdZ0C3%2F2rrL3QmA20dEQtYXqq4vng0GUwHYP1USoK8B2JRt%2Fhu%2FPS1v9UsfOc54E743j%2BmMbwA2AVsBOpL4kxbRyQJ7IxHk%2BfHlWFLrNtW%2BLCOMuu46dS8g%2BG%2BM6SvnKeibuEphU0KI9MYXwqcQvVLqNaXygJUa1DdiOrpto7Iw%2BMAKLoSCE2lsJAZxHGrsWy3CGwFhoEl00R%2BP7ASkb8jElGROxBZhchmRF5HpBr4ZVtH5A7nf5QojeW0FXMjiG0jtnvhxWce6y%2BFdWrvD4aXqWoEGEbkflHdLPBV4E8qskegU1X%2FCHwA2GLNhpZN3kMsG8ty0jM%2Fb7KqpOso8HEVeQWRRxSWo7o7Hk1mgZ03bn4sgDKlNJoJIjZiWdYsKssTEUTEE7j2k2jy9%2FFo0heRvSKyfhSjvF7as2Kswn8qBJOTUEYdEgGxls8CwOlSjkRKbHhjfHCMk9Yov6i5CeBYbJ0HnJ2S990QqgqwaO0T%2B%2BdPZz0eTXrA06guVtVTrQfDO1o7IntU9QDwPICq3okqpqi91oS3%2BdhUSu2KGlCDmkBUzX0zhSAeTXYAG0RkGIgJPCawPR5NHijlyQMKFP3gDxOJ6KeCbpuYkE5VA4XMwCgli4SBxIwgvnj0CHCkrSNixaPJm71A68GwK6qfN0bxBvO%2Fkcl9QPevJzGiKqn%2FnAVjENtNIdJUu%2FjuFLAbSB6LrZt1I9p2MNwKxHMjhUvpK%2F5d1hQ5v00hNy4RRahsbMIEeYKCV2e51d9W%2BIJCi4I%2Fa%2BMdkQZEdplA8YbyuxJ7eswkAMdj6y4CWybK3ep5iBOibtn7cKvqtwS5lA36gqCpOTx%2BLwBLMgP5kyavP5uWfJpj3fuAJ8bK8qmrVNTMZ6TvDGqCP6vq%2FScPfdefpfe7FbZnh%2FIjXr9%2Fb6K95yKAXe7AXZ94%2FLhAlcBHS0yAWFaJEhzy6Wu3q5p7lq76SOLy2ZcL5fSs37mpds2mlfsFfTI3XPAz%2Ff76ZHvPK7Nuy1ti3Y8CB4BFNxISEYq5FF5%2FL37q6gU1wVbU%2FO70kR%2FfzPZ7P%2Fd0Y9N77c0NCy5%2B03YKSzOD%2FvXcUOGzifaeE3P%2BmLTEuhvAPCXif0U1tEjHHDNFn4J3HVPIXRG74oztutna%2BoGmmvp%2F3xOqfsPNe3myg%2FmXirmgNdH%2BUu9b%2Bpo98q21rlvbFDZy%2Bwal4iHLDs2zHAexFMvKYztDOFYfppiikC0W8%2BniiYJvnk2293S%2FrZ9TgE9vW2uhvAfh%2FVjcJiLz1WgR5SrKG8DJxJ6e6zPp%2BS%2FBJqLOE9lRNgAAAABJRU5ErkJggg%3D%3D&labelColor=white&color=green&link=https%3A%2F%2Fchameleoncloud.org%2Fexperiment%2Fshare%2Fc0b5a325-b42c-4d44-bbb1-f2d9be7911d4">
 First, you'll run the `reserve.ipynb` notebook to bring up a resource on Chameleon and configure it with the software needed to run this experiment. At the end of this notebook, you'll set up an SSH tunnel between your local device and a Jupyter notebook server that you just created on your Chameleon resource. Then, you'll open the notebook server in your local browser and run the sequence of notebooks you see there.
