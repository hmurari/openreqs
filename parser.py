import yaml
import pprint

class Parser():
    def __init__(self, req_file):
        self.req_file = req_file
        self.data = None

    def read_file(self):
        try:
            with open(self.req_file, 'r') as f:
                self.data = yaml.load(f, yaml.SafeLoader)

        except Exception as ex:
            print('Exception occurred during file read: ' + str(ex))

    def validate(self):
        # To be implemented.
        pass

    def parse(self):
        self.read_file()
        self.validate()
        self.states = []
        for state in self.data['states']:
            _state_name = list(state.keys())[0]
            _state = state[_state_name]

            if 'actions' not in _state.keys():
                continue

            _actions = []
            for action in _state['actions']:
                _action_name = list(action.keys())[0]
                _action_ret = action[_action_name]['return']
                _actions.append({'name' : _action_name,
                                 'next' : _action_ret})

            self.states.append({
                'state' : {
                    'name' : _state_name,
                    'actions' : _actions
                }
            })
        return self.states

    def nice_print(self):
        pprint.pprint(self.states)


if __name__ == '__main__':
    parser = Parser('openreq-ecommerce.yml')
    parser.parse()
    parser.nice_print()