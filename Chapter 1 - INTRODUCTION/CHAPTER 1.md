# CHAPTER 1
## INTRODUCTION

### 1.1 Research Background

Rainfall data collection in Malaysia has been meticulously conducted over several decades, providing a comprehensive and robust dataset that is invaluable for hydrological studies. The Hydrology and Water Resources Division of the Department of Irrigation and Drainage (DID), Malaysia, has been instrumental in this effort, installing hydrological stations across the country to monitor and record rainfall patterns. This extensive dataset forms the foundation for numerous hydrological and climatological analyses, enabling researchers to investigate the intricacies of Malaysia's weather patterns and their implications for water resource management.

Understanding rainfall patterns is crucial for deciphering climate dynamics, particularly in regions where weather patterns significantly impact the environment and human activities. Accurate rainfall analysis is essential for water resource management, flood risk assessment, and infrastructure planning. Conventional methods of analyzing rainfall data, such as the method of moments and maximum likelihood estimation, have traditionally focused on Annual Maximum Series (AMS). This approach has been beneficial in various climatic contexts, providing valuable insights into extreme weather events and their frequency. However, its application in regions with distinct climatic characteristics, such as tropical areas, may not fully capture the nuances of rainfall patterns.

This research centers on Terengganu, a state in Malaysia located near the equator, renowned for its tropical climate and consistent rainfall patterns. The unique precipitation regime of Terengganu, characterized by frequent and intense rainfall events, poses a challenge to conventional rainfall analysis methods. The tropical climate results in a regularity and intensity of rainfall events that differ significantly from those in temperate regions. Consequently, conventional methods, which often focus on annual maximum values, may not adequately account for the frequent heavy rainfall events typical of tropical climates.

The L-moments method is a statistical approach that offers advantages over conventional moment-based methods, particularly in its robustness to outliers and reduced sensitivity to sample size. L-moments are linear combinations of probability-weighted moments (PWMs) that provide a more stable basis for parameter estimation in extreme value analysis. This method has shown effectiveness in various hydrological studies, particularly in analyzing extreme weather events. However, its application to daily rainfall data in a tropical setting remains less explored. The primary motivation behind this research is the hypothesis that daily rainfall data in a tropical climate, such as that of Terengganu, may provide more insightful information about extreme weather events compared to Annual Maximum Series data. This hypothesis is grounded in the frequent occurrence of heavy rainfall in tropical regions, which contrasts with the less frequent extreme events in temperate regions.

Understanding the return periods of extreme rainfall events is critical for flood risk management and water resource planning. The frequent heavy rainfall in Terengganu necessitates a reevaluation of standard analytical approaches. This research aims to bridge the gap by adapting and applying the L-moments method to daily rainfall data in Terengganu. By focusing on daily data, the study seeks to capture the full spectrum of rainfall events, providing a more accurate representation of the region's rainfall patterns and extreme events.

The significance of this research extends beyond local climate and environmental studies. The findings could have broader applications in similar tropical settings globally, offering new insights into rainfall analysis and extreme weather event prediction. By improving the understanding of rainfall patterns in tropical climates, this research could contribute to more effective water resource management, better flood risk assessment, and enhanced infrastructure planning in these regions.

The proposed research involves a detailed analysis of both Annual Maximum Series and daily rainfall data collected by the DID in Terengganu. The study adapts the L-moments method to suit the tropical context, evaluating its effectiveness in capturing the nuances of rainfall patterns. The research compares the results obtained using daily data with those derived from Annual Maximum Series data, highlighting the differences and potential advantages of each approach.

In summary, this research aims to enhance the prediction of extreme precipitation events in frequency analysis by leveraging both Annual Maximum Series and daily rainfall data and applying the L-moments method to a tropical climate. The expected outcomes include a more accurate representation of rainfall patterns in Terengganu and potentially other tropical regions, leading to improved water resource management and flood risk mitigation strategies. This research contributes not only to the academic understanding of tropical rainfall but also provides practical solutions for managing the unique challenges posed by tropical climates.

### 1.2 Problem Statement

Rainfall data analysis is a fundamental aspect of hydrology, critical for understanding and managing water resources, predicting flood risks, and planning infrastructure. Conventional methods of rainfall data analysis, particularly those that utilize Annual Maximum Series (AMS), have long been the standard in studying extreme weather events. These methods have been developed and refined primarily within the context of temperate climates, where extreme weather events are relatively infrequent and exhibit considerable variability. However, the application of these conventional methods in tropical climates, such as that of Terengganu, Malaysia, reveals significant limitations and discrepancies.

Terengganu, located on the east coast of Peninsular Malaysia, experiences a tropical monsoon climate characterized by frequent and intense rainfall events. The region is subject to heavy and persistent rainfall during the monsoon season, which significantly differs from the sporadic and less predictable rainfall patterns of temperate regions. This climatic distinction challenges the applicability and effectiveness of traditional rainfall analysis methods. Conventional approaches, which often rely on Annual Maximum Series data to assess extreme events, may not accurately capture the true nature and frequency of rainfall patterns in tropical regions.

The primary issue arises from the fundamental difference in the behavior of rainfall events. In temperate climates, extreme rainfall events are typically rare and can be effectively represented using annual maxima. However, in tropical regions like Terengganu, multiple extreme rainfall events can occur within a single year. Relying solely on Annual Maximum Series can lead to an underestimation of the frequency and intensity of extreme rainfall events. This misrepresentation has critical implications for hydrological modeling, water resource management, and flood risk assessment. It can result in inadequate infrastructure design, insufficient flood preparedness measures, and overall mismanagement of water resources.

Furthermore, the traditional statistical models and probability distributions used in conventional rainfall analysis may not be suitable for the unique rainfall characteristics of tropical climates. The high intensity and frequency of rainfall events in these regions necessitate alternative analytical frameworks that can provide a more accurate representation of the data. There is a growing need for methods that can account for the continuous and high-volume nature of tropical rainfall, offering more reliable predictions and assessments.

This discrepancy in rainfall data analysis highlights a critical gap in current hydrological practices. There is an urgent need to develop and validate new methodologies that are tailored to the unique climatic conditions of tropical regions. By addressing this gap, researchers and practitioners can improve the accuracy of rainfall predictions, enhance flood risk management, and ensure the sustainable management of water resources in tropical climates.

This thesis investigates the limitations of conventional rainfall analysis methods in the context of tropical climates, with a specific focus on Terengganu, Malaysia. It seeks to develop and validate alternative analytical frameworks using L-moments that can more accurately capture the characteristics of tropical rainfall. Through comprehensive data analysis and model development, this research contributes to a better understanding of rainfall patterns in tropical regions and provides practical solutions for improved water resource management and flood risk assessment.

### 1.3 Research Objectives

The primary objectives of this research are as follows:

i. To estimate the distribution parameters of the rainfall datasets using the L-moments parameter estimation method.

ii. To identify the most accurate distribution model for the rainfall datasets using suitable performance evaluation metrics, specifically the Mean Absolute Deviation Index (MADI) and Mean Squared Deviation Index (MSDI).

iii. To conduct return period analysis using the most accurate distribution model to estimate extreme rainfall quantiles for various return periods.

iv. To evaluate and quantify the degree of overestimation in return period analysis when using the Annual Maxima (AM) approach relative to daily rainfall data.

### 1.4 Research Questions

This research addresses the following questions:

i. What are the estimated parameter values for the distributions at each rainfall station in Terengganu, Malaysia, using the L-moments method?

ii. Which distribution model most accurately fits the rainfall data for each station in Terengganu, Malaysia, based on goodness-of-fit criteria?

iii. What are the estimated return periods and corresponding quantiles of extreme rainfall events for each rainfall station in Terengganu, Malaysia?

iv. What is the degree of overestimation in return period analysis when using the Annual Maxima (AM) approach relative to daily rainfall data?

### 1.5 Significance of Study

This research addresses a gap in frequency analysis methodologies, which often rely exclusively on Annual Maximum Series hydrological data. Originally, this approach was developed and popularized by researchers from temperate climate regions, where heavy rainfall occurs once every several years. However, in many tropical regions, multiple heavy rainfall events occur throughout the year. Research using tropical region data often employs models designed for temperate region rainfall analysis, potentially leading to misinterpretations of rainfall behavior. This discrepancy arises because the models may fail to capture some of the extreme events within a year, as the data granularity may be insufficient.

The significance of this study is further discussed as follows:

**a) Methodological Adaptation for Tropical Climates**

There is a pressing need for methodological innovations that account for the unique characteristics of tropical climates. By focusing on both Annual Maximum Series and daily rainfall data, this research provides a more comprehensive understanding of precipitation patterns, which is crucial for accurate weather forecasting, water resource management, and disaster preparedness. The application of L-moments methodology to tropical rainfall data represents an advancement in statistical hydrology, offering a more robust approach to parameter estimation that is less sensitive to outliers and sample size limitations.

**b) Enhanced Understanding of Extreme Weather Events**

The analysis of both Annual Maximum Series and daily data using the L-moments method offers new insights into the frequency, intensity, and return periods of extreme rainfall events in Terengganu. This understanding is vital for infrastructure planning, agricultural activities, and developing effective strategies to mitigate the impacts of climate change. By comparing results from both data types, the research provides a comprehensive assessment of extreme rainfall characteristics in tropical regions.

**c) Global and Local Relevance**

While this study is geographically focused on Terengganu, the findings have broader implications. Adapting analytical techniques for tropical climates can benefit other regions with similar climatic conditions. Moreover, the methodological insights gained from this study contribute to the global discourse on climate science, particularly in understanding and managing the impacts of extreme weather events in tropical regions. The research methodology can be replicated in other tropical regions facing similar challenges in rainfall frequency analysis.

**d) Practical Applications**

The findings of this research have direct applications in flood risk assessment, water resource management, and infrastructure design. Accurate estimation of extreme rainfall quantiles for various return periods enables engineers and planners to design appropriate drainage systems, dams, and other water-related infrastructure. The improved understanding of rainfall patterns contributes to better disaster preparedness and mitigation strategies in tropical regions.

### 1.6 Scope of Study

This study focuses on analyzing rainfall patterns in Terengganu, Malaysia, a region characterized by a tropical monsoon climate with frequent and intense rainfall events. The research is centered on the following specific areas:

**Geographical Scope**

The study encompasses multiple rainfall stations located throughout Terengganu, Malaysia. Data from twenty rainfall stations managed by the Department of Irrigation and Drainage (DID), Malaysia, are analyzed. These stations are distributed across various locations in Terengganu, providing a comprehensive representation of rainfall patterns in the region.

**Temporal Scope**

The research utilizes historical rainfall data collected over several decades by the DID. Both Annual Maximum Series (AMS) and daily rainfall series are analyzed to provide a comprehensive assessment of rainfall characteristics and extreme event frequencies.

**Methodological Scope**

The study employs the L-moments method for parameter estimation and distribution fitting. Nine probability distributions are evaluated: Gumbel (GUM), Normal (NOR), Exponential (EXP), Generalized Extreme Value (GEV), Generalized Logistic (GLO), Generalized Normal (GNO), Generalized Pareto (GPA), Pearson Type III (PE3), and Kappa (KAP). The goodness-of-fit assessment is conducted using the Mean Absolute Deviation Index (MADI) and Mean Squared Deviation Index (MSDI) to identify the most appropriate distribution for each station.

**Analytical Scope**

The research includes:
- Calculation of L-moments (L1, L2, L3, L4) and L-moment ratios (L-skewness and L-kurtosis) for each station
- Estimation of distribution parameters using L-moments
- Goodness-of-fit evaluation using MADI and MSDI
- Quantile estimation for various return periods (2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 years)
- Comparison between Annual Maximum Series and daily rainfall data analysis results

**Limitations**

The study is limited to:
- Rainfall data from Terengganu, Malaysia, and may not be directly applicable to other regions without validation
- The use of L-moments method exclusively; other parameter estimation methods are not compared
- The nine distributions specified; other probability distributions are not considered
- Historical data availability; future climate change scenarios are not explicitly addressed

This scope ensures a focused and comprehensive analysis while maintaining practical applicability to water resource management and flood risk assessment in tropical regions.

