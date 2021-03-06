import logging

from report2sqaaas import utils as sqaaas_utils


logger = logging.getLogger('sqaaas.reporting.plugins.licensee')


class LicenseeValidator(sqaaas_utils.BaseValidator):
    valid = False
    threshold = 50

    def parse(self, file_name):
        return sqaaas_utils.load_json(file_name)

    def validate(self):
        try:
            data = self.parse(self.opts.stdout)
            at_least_one_license = False
            trusted_licenses_no = 0
            for license_data in data['matched_files']:
                if not license_data.get('matcher', None):
                    logger.warn(
                        'Matcher data not found for file <%s>. '
                        'Skipping..' % license_data['filename']
                    )
                    continue
                if license_data['matcher']['confidence'] > self.threshold:
                    at_least_one_license = True
                    trusted_licenses_no += 1
            if at_least_one_license:
                self.valid = True
        except ValueError as e:
            data = {}
            logger.error('Input data does not contain a valid JSON: %s' % e)

        return {
            'valid': self.valid,
            'data_unstructured': data
        }
