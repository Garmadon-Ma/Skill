# IEEE revision response-letter format

Use this guide only for response-letter construction, reformatting, and auditing. All examples are generic and must be adapted to the actual decision letter.

## 1. Overall letter order

Use the following order when the corresponding material exists:

1. title and manuscript identification;
2. short letter to the editor;
3. editor or associate editor comments;
4. reviewer sections in the original order;
5. major and minor comments in the original order;
6. `\end{document}` after the final Changes block.

Do not create editor, associate editor, major-comment, or minor-comment sections that are absent from the source decision letter.

## 2. Preamble and caption conventions

Retain a working preamble instead of replacing it wholesale. For a new letter based on `reviewresponse`, the following is a compact starting point:

```latex
\documentclass[a4paper,twoside,10pt]{reviewresponse}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{amsmath,amssymb}
\usepackage{array,booktabs,makecell,multirow}
\usepackage{caption,subcaption,graphicx}
\usepackage{soul,xcolor,hyperref}
\usepackage[normalem]{ulem}
\usepackage{setspace}
\useunder{\uline}{\ul}{}

\captionsetup[figure]{
  labelfont={bf},labelformat={default},labelsep=period,
  name={Fig.},justification=raggedright,singlelinecheck=false
}
\renewcommand{\thetable}{\Roman{table}}
\captionsetup[table]{
  labelfont={bf},labelformat={default},labelsep=space,name={TABLE}
}
```

Add packages only when the letter actually uses them. Do not duplicate existing package declarations. If `[H]` float placement is required, also load `\usepackage{float}`; otherwise prefer standard placements such as `[htbp]`.

Before using this preamble, confirm that `reviewresponse.cls` is available beside the response letter or on the TeX search path. If it is unavailable, do not silently create an incompatible class. Preserve another working response class when one exists, or ask the user whether to use a standard `article` fallback.

## 3. Cover page

```latex
\begin{document}
\thispagestyle{plain}

{\Large
\title{{\Large{RESPONSE TO THE REVIEW COMMENTS OF\\
``<MANUSCRIPT TITLE>'',\\
submitted to <IEEE JOURNAL NAME>}}}
\date{Paper ID: <MANUSCRIPT ID>}
\maketitle

\begin{spacing}{0.9}
Dear Editor:\par
\vspace{1em}
\hspace*{2em}<BRIEF COVER MESSAGE>\par
\vspace{3em}
\noindent Yours sincerely,\par
\vspace{1em}
\noindent <AUTHOR NAMES>
\end{spacing}
}
```

The cover message should thank the editor and reviewers, state that a point-by-point response follows, and briefly note that revisions are identified. Do not summarize every technical change on the cover page.

Replace every angle-bracket placeholder before delivery.

## 4. Reviewer and comment hierarchy

```latex
\newpage
\section{Responses to the Comments from Reviewer 1}

\subsection*{Major Comment 1: <SHORT DESCRIPTIVE TITLE>}
\rcomment{\color{red}
<REVIEWER COMMENT PRESERVED VERBATIM IN VISIBLE WORDING>
}

\textbf{Response:}
<DIRECT RESPONSE>

\textbf{Changes in the manuscript:}
The corresponding revised text is highlighted in red below.

\begin{itemize}
\item \textbf{<ACTION AND LOCATION>.}
\textcolor{red}{<EXACT REVISED WORDING>}
\end{itemize}
```

Use `Major Comment N`, `Minor Comment N`, or the source letter's original category. A descriptive title helps navigation but must not replace the verbatim comment.

Escape LaTeX-special characters in copied comments without changing their visible wording:

```latex
95\%, parameter\_name, A \& B, item \#2
```

Preserve equations and symbols accurately in math mode. Do not place a paragraph break inside one `\uline{...}` command.

If the response class does not define `\rcomment`, inspect its supported comment environment before adding a custom macro. Preserve an existing working implementation.

## 5. Multi-part response

For a comment with several demands:

```latex
\textbf{Response:}
We thank the reviewer for this constructive comment and address each point below.

\begin{itemize}
\item \textbf{Clarification of the method.}
<DIRECT CONCEPTUAL ANSWER.>

\item \textbf{Additional evaluation.}
<EXPERIMENTAL SETTING, RESULTS, AND INTERPRETATION.>

\item \textbf{Scope and limitation.}
<PRECISE BOUNDARY OF THE CLAIM.>
\end{itemize}
```

Replace generic item headings with headings that describe the actual issue. Keep an item only when it corresponds to a distinct part of the review.

Selective emphasis:

```latex
\uline{We added the requested comparison under the same evaluation protocol and report it in Table~\ref{tab:additional-comparison}.}
```

Underline the direct answer or new evidence, not the entire paragraph.

## 6. Changes block

When exact revised wording is available:

```latex
\textbf{Changes in the manuscript:}
The corresponding revised text is highlighted in red below.

\begin{itemize}
\item \textbf{Revise the discussion in Section V-C.}
\textcolor{red}{<EXACT TEXT AS IT APPEARS IN THE REVISED MANUSCRIPT>}

\item \textbf{Add the requested comparison table to Section V-C.}
\end{itemize}
```

When the user has not provided final manuscript wording, clearly use a draft marker during work and remove it before delivery. Never present a paraphrase as an exact manuscript quotation.

If no manuscript change is required, retain the block but state the reason plainly:

```latex
\textbf{Changes in the manuscript:}
No manuscript change was required because the requested information was already provided in Section V-C. We have clarified its location in the response above.
```

Only use this form when no change was actually made. Do not use it to avoid a requested correction.

The response letter is a separate LaTeX document. A label such as `\ref{sec:discussion}` defined only in the manuscript will be undefined in the response letter. For manuscript-only locations, use the verified displayed designation, such as `Section V-C of the revised manuscript`. Preserve the exact visible wording of a revised passage, but render manuscript-local references and citations in a form that compiles correctly in the response letter.

The same distinction applies to numbering. A table reproduced in the response letter can have a different number from the corresponding table in the revised manuscript. Use the response letter's automatic `Table~\ref{...}` when discussing the reproduced table, and use a separately verified designation when describing its location in the revised manuscript.

The action heading says what changed and where. The red passage shows the actual wording. Reviewer-facing reasoning belongs in the Response block.

## 7. Tables

Use automatic numbering and a label directly after the caption:

```latex
\begin{table}[htbp]
\centering
\captionsetup{font=footnotesize}
\caption{\\\textbf{COMPARISON UNDER THE REQUESTED SETTING.}}
\label{tab:additional-comparison}
\footnotesize
\renewcommand{\arraystretch}{1.2}
\setlength{\tabcolsep}{5pt}
\begin{tabular}{@{}lccc@{}}
\toprule
Method & Setting A & Setting B & Setting C \\
\midrule
Baseline 1~[1] & <VALUE> & <VALUE> & <VALUE> \\
Baseline 2~[2] & <VALUE>$^{\dagger}$ & <VALUE> & <VALUE>$^{\dagger}$ \\
Proposed method & \textbf{<BEST>} & \textbf{<BEST>} & \textbf{<BEST>} \\
\bottomrule
\end{tabular}
\par\vspace{2pt}\noindent\makebox[\textwidth][c]{\footnotesize
Note: The best result is shown in bold and the second-best result is marked with $\dagger$.}
\end{table}
```

Introduce the table before or near it:

```latex
Table~\ref{tab:additional-comparison} reports the requested comparison under the same evaluation protocol. <STATE THE OBSERVATION AND ITS RELEVANCE TO THE COMMENT.>
```

Table rules:

- Do not write a response-letter table number inside `\caption*`.
- Do not use a manual `\hyperlink` as a substitute for `Table~\ref{...}`.
- Keep method citations beside method names when citations are used in the letter.
- Recompute best and second-best markings after adding, deleting, or changing a row.
- Include the ranking note only when the table uses those markings.
- Use `\resizebox` only when normal column spacing and font sizing cannot fit the table legibly.
- Prefer collision-resistant response labels such as `tab:r2c3-additional-comparison`, where the prefix identifies the reviewer and comment.

## 8. Figures

```latex
Fig.~\ref{fig:additional-analysis} provides the requested visual evidence. <EXPLAIN THE OBSERVATION.>

\begin{figure}[htbp]
\centering
\includegraphics[width=0.76\textwidth]{<FIGURE FILE>}
\caption{<SELF-CONTAINED FIGURE CAPTION>.}
\label{fig:additional-analysis}
\end{figure}
```

For related panels, use one multi-panel figure with one overall caption and number. Center panel titles relative to their images and leave visible vertical space between a title and its image.

The surrounding response must explain what the figure shows and how it answers the comment. Do not add an unreferenced or uninterpreted figure.

If a figure is mentioned but not reproduced in the response letter, write its verified manuscript designation explicitly, for example `Fig.~7 in the revised manuscript`. Do not create a `\ref` to a label that exists only in another LaTeX document.

Prefer collision-resistant labels such as `fig:r1c2-additional-analysis` for figures created inside the response letter.

## 9. Equations

Use an equation only when it materially clarifies the response:

```latex
\begin{equation}
g(\mathbf{x}) = h\!\left(f_{\theta}(\mathbf{x})\right).
\label{eq:response-definition}
\end{equation}
```

Keep notation consistent within the response letter and with any quoted revised passage. Check dimensions, subscripts, superscripts, delimiters, and punctuation. Explain why the equation resolves the reviewer concern.

## 10. Final response-letter audit

- Cover-page placeholders have been removed.
- Editor and reviewer comments are in their original order, verbatim in visible wording, safely escaped for LaTeX, and red.
- Every comment has one Response block and one Changes block.
- Every part of a multi-part comment is answered.
- Key new answers are selectively underlined, while ordinary response text remains black.
- Exact revised wording is red and is not mixed with response-only reasoning.
- Names, numbers, units, equations, citations, and claimed locations are internally consistent.
- Tables, figures, sections, and equations defined in the response letter use automatic references.
- Manuscript-only items use verified displayed designations and are clearly identified as belonging to the revised manuscript.
- Every float is referenced and interpreted.
- Labels are unique and placed after captions.
- No placeholder, temporary note, duplicated response, obsolete value, or unsupported claim remains.
- The response letter compiles without fatal errors or undefined references or citations.

