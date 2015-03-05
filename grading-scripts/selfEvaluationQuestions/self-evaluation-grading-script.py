from collections import namedtuple
Skill = namedtuple('Skill', ['name', 'expected_stage', 'feedback_for_expected', 'feedback_for_below',
                             'feedback_for_above', 'recommendation_if_below'])

##########################################################
# You should only modify the GLOBAL variables below here #
##########################################################

URL_TO_TOP_IMAGE = "http://i.imgur.com/fdGeWES.png"
STAGE_NAMES = ['Ignorance', 'Awareness', 'Ability', 'Fluency']
DEFAULT_RECOMMENDATION = "You're doing great! Continue with the Nanodegree!"
SKILLS = [Skill(name                    = "HTTP, Servers, and Browsers",
                expected_stage          = STAGE_NAMES[1],
                feedback_for_expected   = """Great! You are familiar with these ideas but can't yet do much with them. That's exactly where you should be.""",
                feedback_for_below      = """The next lesson in the Nanodegree assumes you're at least familiar with these terms.""",
                feedback_for_above      = """We were only expecting 'Awareness' at this point. It's great that you're already beyond that!""",
                recommendation_if_below = """You should rewatch the previous lesson."""),
          Skill(name                    = "Using HTML tags",
                expected_stage          = STAGE_NAMES[1],
                feedback_for_expected   = """You only need to know that HTML tags exist and what they look like for the next lesson.""",
                feedback_for_below      = """If you are completely unaware of how to use HTML tags, the next lesson will be more difficult than it needs to be.""",
                feedback_for_above      = """Your ability with using HTML tags will help you in the next lesson.""",
                recommendation_if_below = """You should rewatch the previous lesson.""")
          ]
COMPLETED = True # This is a global but it shouldn't require modifying.

##########################################################
# You should not need to modify anything below here      #
##########################################################

def get_responses_by_skill(widget_inputs, stage_names):
    """widget_inputs is a global variable that is accessible
    by the grader code"""
    assert(len(widget_inputs) % len(stage_names)) == 0
    NUM_SKILLS = len(widget_inputs) / len(stage_names)
    widget_list = []
    for k, v in widget_inputs.items():
        widget_list.append((k,v))
    widget_list.sort()
    checked_list = [v for k,v in widget_list]
    responses = []
    for i in range(NUM_SKILLS):
        responses.append(None)
        for j, s in enumerate(stage_names):
            checked = checked_list[i*len(stage_names) + j]
            if checked:
                responses.pop()
                responses.append(stage_names[j])
                break
    return responses

def make_feedback_message(responses, skills, stage_names):
    """feedback messages are written in Markdown"""
    recommendation = DEFAULT_RECOMMENDATION
    if URL_TO_TOP_IMAGE:
        markdown = "# ![](%s) Feedback\n\n" % URL_TO_TOP_IMAGE
    else:
        markdown = "# Feedback\n\n"
    assert len(responses) == len(skills)
    for i, resp in enumerate(responses):
        skill = skills[i]
        markdown += "### %s\n\n" % skill.name
        markdown += "**You Said:**\tStage %i\t(%s)\n\n" % (stage_names.index(resp), resp)
        markdown += "**Expected:**\tStage %i\t(%s)\n\n" % (stage_names.index(skill.expected_stage), skill.expected_stage)
        stated_level = stage_names.index(resp)
        expected_level = stage_names.index(skill.expected_stage)
        if stated_level < expected_level:
            recommendation = skill.recommendation_if_below
            COMPLETED = False
            feedback_for_skill = skill.feedback_for_below
        elif stated_level == expected_level:
            feedback_for_skill = skill.feedback_for_expected
        else:
            feedback_for_skill = skill.feedback_for_above
        markdown += "*%s*\n\n" % feedback_for_skill
        markdown += "****\n\n"
    markdown += "###What Next?\n"
    markdown += recommendation
    return markdown

def evaluate_and_give_feedback(widget_inputs):
    responses = get_responses_by_skill(widget_inputs, STAGE_NAMES)
    feedback_markdown = make_feedback_message(responses, SKILLS, STAGE_NAMES)
    grade_result["correct"] = None   # This line ensures that there is no "Correct" or "Try Again!" message
    grade_result["completed"] = COMPLETED # This line determines whether subway nav dot is filled in.
    grade_result["comment"] = feedback_markdown
    pass

evaluate_and_give_feedback(widget_inputs)


