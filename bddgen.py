from parser import Parser
import pprint

class BDDGen():
    def __init__(self, req_file):
        self.parser = Parser(req_file)
        self.data = self.parser.parse()

    def nice_print(self):
        pprint.pprint(self.data)

    def gen_code(self):
        for state in self.data:
            state_name = state['state']['name']
            feature_name = 'Feature: '  + state_name.title().replace('_', ' ')
            file_name = state_name + '.feature'

            steps = []
            given = 'Given I am on page "{}"'.format(state_name.title())
            for action in state['state']['actions']:
                scenario = 'Scenario: ' + action['name'].title()
                when = 'When I ' + action['name']
                then = 'Then my next page will be ' + action['next']
                steps.append({
                    'scenario' : scenario,
                    'given' : given,
                    'when' : when,
                    'then' : then
                })

            with open(file_name, 'w') as f:
                f.write(feature_name)
                f.write('\n')
                for step in steps:
                    f.write('\t' + step['scenario'] + '\n')
                    f.write('\t\t' + step['given'] + '\n')
                    f.write('\t\t' + step['when'] + '\n')
                    f.write('\t\t' + step['then'] + '\n')
                    f.write('\n')

if __name__ == '__main__':
    bddgen = BDDGen('openreq-ecommerce.yml')
    bddgen.nice_print()
    bddgen.gen_code()
