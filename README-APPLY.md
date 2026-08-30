# MAC Unit I — Final Answer + Textbook Problem-Set Reference

This delta makes two global PankusDesk improvements and applies them to MAC Unit I:

1. Fully worked solutions end with a visually distinct **bold final answer/result** whenever a determinate result exists.
2. In-scope prescribed-textbook problem sets are linked from the theory page at the same logical point where they appear in the textbook. Problems 2.4 (p. 44, Q1–Q9) now appears immediately after the Grewal Normal Form section, before the supporting class-note section.

It also extends the shared schemas/renderers so the rules apply across subjects going forward.

## Apply

Dry run:

    rsync -avhn mac-finalanswer-problemref-delta/ Pankusdesk/

Real sync:

    rsync -avh mac-finalanswer-problemref-delta/ Pankusdesk/

No `--delete` is used.
