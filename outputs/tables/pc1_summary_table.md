# PC1 Summary Table

| City | PC1 corr. with LST (\|r\|>0.5) | PC1 corr. with HI (\|r\|>0.5) | PC1 corr. with HI−LST_z (\|r\|>0.5) | PC1 dominant in SHAP (rank-1) |
|---|---|---|---|---|
| Atlanta | Yes | No | Yes | Yes |
| Boston | Yes | No | Yes | Yes |
| Chicago | No | No | No | Yes |
| Dallas | Yes | No | Yes | Yes |
| Houston | Yes | No | Yes | Yes |
| Las Vegas | No | No | No | No |
| Los Angeles | No | No | No | No |
| Miami | Yes | No | Yes | Yes |
| New York | No | No | No | Yes |
| Phoenix | No | No | No | No |
| San Francisco | No | No | No | No |
| Seattle | No | No | No | Yes |

---

**Definitions**

- **PC1**: The first principal component, i.e., the component explaining the most variance in the input feature matrix.
- **PC1 corr. with LST / HI / HI−LST_z**: Whether PC1 has a Spearman |r| > 0.5 with that observable across all pixels in the city. Correlation is computed between PC1 scores and the target variable.
  - **LST**: Land Surface Temperature (°C)
  - **HI**: Heat Index (°C)
  - **HI−LST_z**: Standardized difference between Heat Index and LST (the mismatch variable)
- **PC1 dominant in SHAP (rank-1)**: Whether PC1 has the highest mean |SHAP| value among all PCs for that city's RF model.
