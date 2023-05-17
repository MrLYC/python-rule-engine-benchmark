Hit Policy: First
| (input) cart.total | (input) customer.country | (input) customer.tier | (output) fees.flat | (output) fees.percent |
| ------------------ | ------------------------ | --------------------- | ------------------ | --------------------- |
| >1000              | "US"                     | "gold"                |                    | 2                     |
| >1000              | "US"                     | -                     |                    | 3                     |
| -                  | "US"                     | -                     | 25                 |                       |
| >1000              | "CA","MX"                | -                     |                    | 5                     |
| -                  | "CA","MX"                | -                     | 50                 |                       |
| >1000              | "IE","UK","FR","DE"      | -                     |                    | 10                    |
| -                  | "IE","UK","FR","DE"      | -                     | 100                |                       |
| >1000              | -                        | -                     |                    | 15                    |
| -                  | -                        | -                     | 150                |                       |