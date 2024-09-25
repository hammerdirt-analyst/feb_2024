import re


def report_system_prompt(roughdraft):
    system_prompt = (
    "You are a researcher assigned the task of preparing the first draft of a manuscript from a rough draft and answering specific questions "   
    "You will be given a list of information to provide and a list of questions.Provide the information and answer the questions "
    "according to the document provided and the instructions given. The instsructions are marked like this '<!--- INSTRUCTION_START your '"
    "'instructions will be found here INSTRUCTIONS_END -->'. Follow the instructions exactly. "
    "Answer the question completely and use an authoritative voice. Do not invent or make up answers. If you use a web resource you must give the link. "
    "You must give numerical examples from the report when you answer a question about the survey results. "
    "Do not answer the questions twice. If the question is answered in the summary state this. If there are no questions pass, do not make any questions up. "
    "The most important part of this task is transmitting the numerical results correctly to the user. "
    "All answers should be in paragraph form. Here is the document of reference :\n\n" 
    f"{roughdraft}"
    )
    return system_prompt

def split_text_on_phrase(text, phrase="Frequently asked questions"):
    """
    Splits the input text into two parts based on a line containing the provided phrase
    and either ## or ### as the heading marker, allowing for optional newlines around the heading.

    Parameters:
    text (str): The full text to be split.
    phrase (str): The phrase to split the text on. Default is "Frequently asked questions".

    Returns:
    tuple: A tuple containing two strings, the first part before the heading with the phrase
           and the second part including the heading with the phrase and everything after it.
    """
    # Compile a regex pattern to find lines with ## or ### followed by the phrase
    pattern = re.compile(r'(^##+)\s*' + re.escape(phrase) + r'\s*(?:\n|\n\n)', re.IGNORECASE | re.MULTILINE)

    # Find the match
    match = pattern.search(text)
    if not match:
        return text, ''  # If no match is found, return the whole text in the first part

    # Split the text at the position of the matched heading
    split_index = match.start()
    before_phrase = text[:split_index]
    after_phrase = text[split_index:]

    return before_phrase, after_phrase

def report_summary_prompt():

    user_prompt = f"""\n

    Provide a summary of the following sections: Administrative boundaries, Named features, Summary statistics, Municipal results, Material composition.

    The following must be included in the summary:

    * The Name and number of the cities in the report <!--- INSTRUCTION_START The names of the lakes, rivers and parks are in the named features section, the municipal results are in the city total section INSTRUCTIONS_END -->\n
    * The name and number of lakes, rivers or parks in the report : <!--- INSTRUCTION_START The names of the lakes, rivers and parks are in the named features section, the municipal results are in the city total section INSTRUCTIONS_END -->\n
    * The start and end date of the sampling and the name of the survey area(s), the name of the survey areas must have the first letter capitalized.\n
    * The numbar of samples, the average pcs/m, the maximum pcs/m, the standard deviation and the total number of objects identified\n
    * The material composition\n   

    Frequently asked questions:

    1. What were the five most common items found ? <!--- INSTRUCTION_START Provide the name of the object, the fail rate and the percent of total. Convert the fail rate to percent. define the fail rate. INSTRUCTIONS_END -->
    2. Are these objects found on european beaches ? If so is their any data on how many per 100 m of beach ? <!--- INSTRUCTION_START you may use your base knowledge to answer this question, consider OSPAR results from 2022 or 2021 INSTRUCTIONS_END -->
    3. What are possible sources of these specific objects objects ? <!--- INSTRUCTION_START you may use your base knowledge to answer this question INSTRUCTIONS_END -->
    4. Which three cities had the highest average pcs/m ? Which three had the lowest ?


    <!--- INSTRUCTION_START\n

    formatting instructions:

    1. Label the summary 'Sample results' (##)\n
    2. The label for the questions section is 'Frequently asked questions' use markdown formatting for the label (###)\n
    3. Repeat the question (in bold) DO NOT REPEAT the instructions. and then answer\n

    INSTRUCTIONS_END -->
    """
    return user_prompt



def report_stratification_prompt():

    request = (
        "Define sampling stratification and land-use, explain how it applies to the survey results. "
        "Would this be considered urban, rural or mixed ? "
        "What are the two highest pcs/m values in the sampling stratification and trash density table ? What are the land use features and the proportion of buffer they occupy? "
    )

    req_inf = (
        "<!-- INSTRUCTION_START Define sampling stratification in the general sense and explain how it is used in this survey. Define what land use is. "
        "To determine if a location is urban you must sum the proportions of samples for buildings for the rows 60-80% and 80 - 100% of the sampling stratification table. "
        "If this sum is greater than 50% the area is considered urban. To determine if a location is urban you must sum the proportions of samples "
        "for forests for the rows 60-80% and 80 - 100% of the sampling stratification table.If this sum is greater than 50% the area is considered rural. "
        "If both sums are less than 50% the area is considered mixed."        
        " INSTRUCTION_END -->\n"

    )
    insone = (
        "<!-- INSTRUCTION_START Provide examples from the 'sampling stratification and trash density table' consider the results from the buildings, forest, and undefined columns."
        "Find the two highest values and report the proportion of buffer they occupy and the proportion of the samples that were taken."
        " and explain what the values mean. Give two examples from the table. Do not draw any conclusions. Reply in paragraph form."
        " INSTRUCTION_END -->\n"
    )

    instwo = (
        "<!-- INSTRUCTION_START Follow all instructions in the document and reply in paragraph form."
        " INSTRUCTION_END -->\n"
    )

    insthree = (
        "<!-- INSTRUCTION_START Provide examples from the 'sampling stratification and trash density table' consider the results from the buidlings, forest, and undefined columns. "
        "Find the two highest values and report the proportion of buffer they occupy and the average pcs/m."
        " INSTRUCTION_END -->\n"
    )

    insfour = (
        "<!-- INSTRUCTION_START Recall the definition for urban and rural is provided in the document instructions. If the sampling stratification does not meet either criteria, say so and reply with "
        "prportion of the buffer that contains the greates proportion of samples for buildings, forest and undefined "
        " INSTRUCTION_END -->\n"
    )

    questions = (
        f"1. What does the sampling stratification table tell us ?{insone}"
        f"2. How can the information in the sampling stratification and trash density table help identify areas of concern ?{instwo}"
        f"3. Under what landuse conditions would a surveyor expect to find the most trash ?{insthree}"
        f"4. Given the results in the sampling stratification table, were these surveys collected in mostly urban environment or forested?{insfour}"

    )

    formatting_instructions = (
        "\n<!-- INSTRUCTION_START\n"
        "1. Label the summary 'Sampling stratification' (##)\n"
        "2. The label for the questions section is 'Frequently asked questions' (###) \n"
        "3. Repeat the question (in bold) DO NOT REPEAT the instructions. and then answer\n"
        " INSTRUCTION_END -->\n"
    )

    user_prompt = (
        f'{request}{req_inf}\n\n'
        f'{questions}\n\n'
        f'{formatting_instructions}'
    )

    return user_prompt


# grid forecast analysis
def grid_approximation_prompt():

    request = (
        "Explain what a grid approximation is and the method used in this report. "
        "Define what an inference table is, and the role of prior and posterior distributions in building an inference table. "
        "For each prior in report results cite the name of the prior, and the similarity threshold of the prior. "
        "Cite the differences between the different priors "
        "Compare the different posterior distributions to the observed results (in pcs/m) ? Should an increase or decrease be expected ? "
    )

    insone = (
        "<!-- INSTRUCTION_START Consider whether the observed data is likely to be normally distributed or not (use the difference between the median "
        "and mean in summary statistics section). You must cite the values you use in the calculation. Describe the implications on predictions if the data "
        "is normally distributed or not, given the units and the context consider the case where the data is normally distributed"
        " INSTRUCTION_END -->\n"
    )

    insthree = (
        "<!-- INSTRUCTION_START Cite the name of the prior and the expected average and median pcs/m. INSTRUCTION_END -->\n"

    )

    insfour = (
        "<!-- INSTRUCTION_START Consider that the prior is comprised only of locations that are in the same geographic boundary. "
        "Recall that the posterior is a weighted average of the prior and likelihood, so if the in-boundary prior predicts an increase "
        "it is likely that elevated values were observed in other locations within the boundary compared to the likelihood "
        " INSTRUCTION_END -->\n"
    )

    insfive = (
        "<!-- INSTRUCTION_START Consider that the prior is comprised only of locations that are outside the geographic boundary. "
        "Recall that the posterior is a weighted average of the prior and likelihood, so if the out-boundary prior predicts an increase "
        "it is likely that locations outside of the region had elevated values compared to the likelihood "
        " INSTRUCTION_END -->\n"
    )

    inssix = (
        "<!-- INSTRUCTION_START You will find the observed pcs/m in the Summary statistics section. For each posterior there is a "
        "section. Consult the table of values in each section. Consider the average pcs/m result of each posterior in relation to the observed average "
        "Cite the numerical differences, given the standard deviation (in pcs/m) how likely is a person to notice the increase or decrease if they take one sample ? "
        " INSTRUCTION_END -->\n"
    )
    questions = (
        "<!-- INSTRUCTION_START Label the questions section 'Frequently asked questions' (###) INSTRUCTION_END -->\n"
        f"1. Why is grid approximation a reasonable modeling technique given the data ?{insone}"
        "2. Do you have an example of other fields or domains that use grid approximation or bayesian methods ?"
        "3. If the data is normally distributed would the predictions from the grid approxmation and the predictions from the normal distribution be different ? If so in what way ?"
        "4. What is the difference between grid approximation and linear or enemble regression ?"
        f"5. With which posterior do we expect to the find most ? The least ?{insthree}"
        f"6. If the in-boundary grid approxmation predicts an increase or decrease, what does that say about the other samples from within the boundary ?{insfour}"
        f"7. If the out-boundary grid approxmation predicts an increase or decrease, what does that say about the other samples from outside of the boundary ?{insfive}"
        f"8. How different are the expected results from the observed results ? Should an increase or decrease be expected ? {inssix}"

    )

    formatting_instructions = (
        "\n<!-- INSTRUCTION_START \n"
        "1. Label the summary 'Forecasts and methods' (##)\n"
        "2. Label the questions section 'Frequently asked questions' (###) \n"
        "3. Repeat the question (in bold) DO NOT REPEAT the instructions. and then answer\n"
        " INSTRUCTION_END -->\n"
    )



    user_prompt = (

        f'{request}{inssix}\n\n'
        f'{questions}\n\n'
        f'{formatting_instructions}'
    )

    return user_prompt


def report_regression_prompt():

    request = (
        "Define cluster analysis (kmeans)"
        "Define linear regression and ensemble regression, explain the basic assumptions of each method"
        "If a regression analysis was conducted what model had the highest r² (the best model) ? What was the mse of the best model ? "
        "If their was a regression analysis conducted, what conclusions can be drawn given the best model ?"
        "Given the r² and MSE of the best model how reliable would predictions be ?"
        "If you have concluded that the regression analysis would be reliable, what are the features that might have the greatest influence on the target variable ?"
    )

    req_inst = (
        "<!-- INSTRUCTION_START Provide concise answers to each request. Label these answers 'Linear and ensemble regression' (##) INSTRUCTION_END -->\n"

    )

    insone = (
        "<!-- INSTRUCTION_START  If their was no regression analysis the report will tell you why. If there is a table, provide that table to user and "
        "write a narrative paragraph of all the results."
        " INSTRUCTION_END -->\n"
    )

    insfour = (
        "<!-- INSTRUCTION_START It is possible that there is no cluster analysis. The report will tell you why. This is a valid answer. "
        "The average pcs/m is given as a table in the cluster analysis subsection and given as objects per meter. "
        "The distribution of land use values is given in the cluster analysis subsection and given as a float value that represents "
        "the average proportion of the buffer zone occupied by the land use category. The paragraph above the table explains how to interpret the table"
        " when you provide the results for the cluster lable the results as % of buffer occupied by land use feature INSTRUCTION_END -->\n"
    )

    questions = (
        "Frequently asked questions\n"
        f"1. What were the r² and MSE of each test ? {insone}"
        f"2. Given the r² and MSE of the different methods employed, how reliable do you think predictions would be based on these models ?\n"
        f"3. Can any conlusions be drawn from these results ?\n"
        f"4. Accroding to the cluster analysis what is the cluster that has the greatest average pcs/m ? What is the distribution of land use values within the cluster ? {insfour}"
    )

    formatting_instructions = (
        "\n<!-- INSTRUCTION_START \n"
        "1. The label for the whole section is 'Linear and ensemble methods' (##)\n"
        "2. The label for the questions section is 'Frequently asked questions' (###) \n"
        "3. Repeat the question (in bold) DO NOT REPEAT the instructions. and then answer\n"
        " INSTRUCTION_END -->\n"
    )
    user_prompt = (

        f'{request}{req_inst}\n\n'
        f'{questions}\n\n'
        f'{formatting_instructions}'
    )

    return user_prompt


def final_draft_prompt(roughdraft):
    system_prompt = (
        "You are a researcher assigned preparing a manuscript from a revised draft. "
        "You are tasked to correct the individual sections of the revised draft for the manuscript. "
        "Ensure that answers are correct by comparing the revised draft to the rough draft. "
        "Ensure that any conclusions are correct by reviewing the instructions in the rough draft and responses in the reivsed draft."
        "Do not change the formatting of the revised draft."
        "There are instructions in the rough draft labeled <!--- INSTRUCTION_START  your instructions are in here INSTRUCTION_END -->. Ensure the insstructions were followed"
        "The rough draft:\n"
        f"{roughdraft}"
    )
    return system_prompt


# grid forecast analysis



def corrections_prompt(document):
    request = (
        "Please check the answers provided in this revised draft to the rough draft that you have. Any numerical float values should be rounded to two places. "
        "Return the document with the corrections please. Do not add any comments about the corrections, just do them and return the corrected document."

    )

    req_inf = (
        "<!-- INSTRUCTION_START We are concerned with numrical results and conclusions. "
        "Ensure that any conclusions are correct according to standard practice and the methods explained in the rough draft instructions. Do not change the markdown formatting of the document."
        " INSTRUCTION_END -->\n"
    )
    user_prompt = (
        f'{request}{req_inf}\n'
        'The revised draft: \n\n'
        f'{document}')

    return user_prompt


def executive_summary_prompt(roughdraft):
    system_prompt = (
        "You are a researcher assigned the task of writing the executive summary of a report from a revised report. "
        "You are tasked to draft the executive summary and ensure that key points in the rough draft do not get excluded. "
        "There are instructions in the rough draft labeled <!--- INSTRUCTION_START  your instructions are in here INSTRUCTION_END -->. Ensure the insstructions were followed"
        "The rough draft:\n"
        f"{roughdraft}"
    )
    return system_prompt




def executive_corrections_prompt(document):
    request = (
        "Make an executive summary of the revised draft below, use four paragraphs.\n"
      
        "Summarize the results from each section, use the following guidelines : \n\n"
        "1. **Sample results:** Include the number of cities, lakes, rivers and parks in the report, the start and end date "
        "of the sampling, the number of samples, the average pcs/m, the maximum pcs/m, the standard deviation and the total number of objects identified.\n "
        "2. **Samping stratification and sampling stratification and trash density:** Define sampling stratification in one sentence. Include the determination of urban or rural classification according to the provided text and the proportions of importance.\n"
        "3. **Linear and ensemble regression:** If a regression analysis was not conducted state the reason. If a regression analysis was conducted "
        "cite the model with the highest r² and the corresponding MSE. Cite features of importance using the permutation feature importance and the model feature importance"
        "If a regression analysis was conducted and you have an r² and MSE, state the reliability of predictions given these results.\n"
        "4. **Forecasts and methods:** Define grid approximation and the method used in the report, concisely and briefly. Explain the hypothesis of each prior. Give the "
        "posterior results for each of the defined priors. Compare the posterior results to the observed results and state whether an increase or decrease is expected.\n"
    )

    req_inf = (
        "<!-- INSTRUCTION_START Label this section Executive summary (##). Your opinion is not needed, only draw conclusions from the data. "
        "Ensure that any conclusions are correct according to standard practice and the methods explained in the rough draft instructions. Keep the executive summary to four paragraphs."
        " INSTRUCTION_END -->\n"
    )

    user_prompt = (
        f'{request}{req_inf}\n'
        'The revised draft: \n\n'
        f'{document}')

    return user_prompt