from ckan.plugins.toolkit import get_action
from ckan.common import config

def get_org_title(id):
    try:
        org = get_action('organization_show')({}, {'id': id})

        return org.get('title', '')
    except Exception:
        return ''

def get_org_logo(id):
    try:
        org = get_action('organization_show')({}, {'id': id})

        return org.get('image_display_url', '')
    except Exception:
        return ''

def get_jira_script():
    jira_script = config.get('ckanext.nextgeoss.jira_issue_tracker')
    return jira_script


def get_add_feedback_url(dataset):
    """
    Create the URL for adding feedback on a dataset via NiMMbus.

    The ID and namespace are currently based on the CKAN instance, but
    in the future they should be updated to use the original ID
    and namespace of the dataset, once we've determined how they'll
    be represented in the metadata.
    """
    feedback_url = 'http://www.opengis.uab.cat/nimmbus/index.htm?target_title={target_title}&target_code={target_code}&target_codespace={target_codespace}&page=ADDFEEDBACK&share_borrower_1=Anonymous'.format(
        target_title=dataset['title'],
        target_code=dataset['id'],
        target_codespace=config.get('ckan.site_url'))

    return feedback_url
