# MAC class-notes accordion cleanup

This delta removes notebook-page-fragment presentation from Unit I class notes and groups each worked class problem into one complete shared-study accordion.

Key changes:
- 25 Aug: two normal-form examples are each single complete accordions.
- 28 Aug: three Gauss–Jordan examples are each single complete accordions.
- 1 Sep: six Gauss-elimination/consistency examples are no longer split into beginning/completion page fragments.
- 2 Sep: three further row-rank examples are complete accordions.
- 4 Sep: headings no longer imply that Example 1 is physically split across notebook pages.
- Global College Build Standard/Checklist now state that notebook page boundaries are provenance only; student-facing class notes are organized by logical lesson/example.

Apply from the folder that contains both this delta and `Pankusdesk`:

    rsync -avhn mac-classnotes-accordion-cleanup-delta/ Pankusdesk/

    rsync -avh mac-classnotes-accordion-cleanup-delta/ Pankusdesk/
