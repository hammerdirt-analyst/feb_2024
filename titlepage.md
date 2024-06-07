# The litter assistant

::::{grid}
:gutter: 0

:::{grid-item-card}



:::
:::{grid-item-card}

```{image} resources/hammerdirt.png
:alt: bob
:class: bg-primary mb-1
:width: 400px
:align: center
```
:::
::::
::::{grid}

:::{grid-item-card}

* https://github.com/hammerdirt-analyst/IQAASL-End-0f-Sampling-2021
* https://github.com/hammerdirt-analyst/cantonal_reports
* https://github.com/hammerdirt-analyst/solid-waste-team
* https://github.com/hammerdirt-analyst/landuse
* plastock project with [ASL](https://asleman.org/)
* https://github.com/hammerdirt-analyst/finding-one-object

:::
:::{grid-item-card}

:::
::::
The UX and final app structure can be tested here (! the llm is not yet attached): [litter assisstant](https://litterassistant.streamlit.app/)

# Checking the assistant

This page is a reference point for testing the accuracy of the chat agent assigned to accompany readers of the federal report. The agent should reproduce the calculations on this page at any time. This includes values not in the federal report. Stakeholders will need to apply these results to their proper geographic or administrative responsibilities. The hammerdirt agent assists in this process.



```{important}

__June 7, 2024:__ 

The data provided to the chat agent is now limited to the data for the cantons in this prototype. 


__PREVIOUS__

__April 17, 2023:__ The app that uses the chat agent is in demo-form. We have abandoned the intial method of defining the prompt through the api. We are now developing a RAG application. A component of the context for the prompt is the results from users request. With this we combine the references from the federal report and any updated references that can be included.

**Changes to class definitions:** Building a RAG application means that we have to consider both the user visualisation of the report and the consumption of that data for the AI model, data_frame or array for the former, .JSON for the latter. These considerations will have a transformative effect on all the code in this module.



November 20, 2023: There is a known issue we are working on now. Remind the assistant to follow intsructions. Specifically in the following cases:

1. Always getting a value of zero for the median sample total
   * The GPT has specific instructions on this
2. Tells you the correct columns are not available
   * The GPT has the column names and definitions from this page

The data has a two column index, somtheing the GPT does not always recognize. An issue has been submitted [issue](https://github.com/hammerdirt-analyst/feb_2024/issues/1)
```

```{note}
The assistants role is to provide mathematical and graphical representations of the data in response to the researchers request. This often involves aggregating values at different levels, combining attributes and the like.

This page allows all users to verify that these complex transactions are happening correctly. The GPT may not use the same method to calculate the final result, but the results should be same.
```
## Default data of hammerdirt GPT:
```


## Questions

contact analyst at hammerdirt