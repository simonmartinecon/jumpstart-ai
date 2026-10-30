* Example data shipped with Stata
sysuse nlsw88, clear
generate lwage = ln(wage)

* Regressions
eststo clear
eststo: regress lwage grade ttl_exp, robust
eststo: regress lwage grade ttl_exp union, robust

* Export a production-ready LaTeX table
esttab using "output/tables/wage_regs.tex", ///
    replace booktabs label se               ///
    keep(grade ttl_exp union)               ///
    mtitles("Baseline" "With union")
