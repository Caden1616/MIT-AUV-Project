# Parse 3 word COMM string and return COMMAND if it is not understood

class AUV(object):
    def __init__(self,latlon=(0.0,0.0),depth=0.0,speed_knots=0.0,heading=0.0,rudder_position=0.0,engine_speed='STOP',engine_direction='AHEAD',datum=(0.0, 0.0)):
        self.latlon=latlon
        self.depth=depth
        self.speed_knots=speed_knots
        self.heading=heading
        self.rudder_position=rudder_position
        self.engine_state=[engine_speed,engine_direction]
        self.__datum=datum
        self.__MAX_SPEED_KNOTS=10

    def engine_command(self, command='COMMAND'):
        self.command=command
        command_array = command.split()

        if command_array[0] == 'ENGINE':

            if command_array[1] == 'SLOW':
                self.speed_knots = self.__MAX_SPEED_KNOTS * 0.25
                self.engine_state[0]='SLOW'

            elif command_array[1] == 'HALF':
                self.speed_knots = self.__MAX_SPEED_KNOTS * 0.50
                self.engine_state[0]='HALF'
            
            elif command_array[1] == 'FULL':
                self.speed_knots = self.__MAX_SPEED_KNOTS
                self.engine_state[0]='FULL'
            
            elif command_array[1] == 'STOP':
                self.speed_knots = self.__MAX_SPEED_KNOTS * 0
                self.engine_state[0]='STOP'
                return self.command
            
            else:
                return 'COMMAND'
            
            if command_array[2] == 'AHEAD' or command_array[2] == 'ASTERN':
                print(command_array[2])
                print(self.engine_state[1])
                if command_array[2] == 'AHEAD' and self.engine_state[1] == 'ASTERN':
                    self.heading+=180
                    self.heading = self.heading % 360
                    self.engine_state[1] = 'AHEAD'
            
                elif command_array[2] == 'ASTERN' and self.engine_state[1] == 'AHEAD':
                    self.heading+=180
                    self.heading = self.heading % 360
                    self.engine_state[1] = 'ASTERN'
                    print(self.engine_state[1])
            
            else:
                return 'COMMAND'
        
        else:
            return 'COMMAND'
        
        return self.command