import orwell.messages.version1_pb2 as protobuff
import orwell.messages.controller_pb2 as pb_controller
import orwell.messages.robot_pb2 as pb_robot
import orwell.messages.server_game_pb2 as pb_server_game
import orwell.messages.server_web_pb2 as pb_server_web


def old_test():
    login = protobuff.login_message()
    login.client_id = 'toto'
    login.wished_robot_type = 'TANK'
    login_msg = login.SerializeToString()
    login_2 = protobuff.login_message()
    login_2.ParseFromString(login_msg)
    assert(login == login_2)

# server-game


def test_team():
    message = pb_server_game.Team()
    score = 3
    num_players = 2
    players = ["JAMBON", "RACLETTE"]
    message.score = score
    message.num_players = num_players
    for player in players:
        message.players.append(player)
    payload = message.SerializeToString()
    message2 = pb_server_game.Team()
    message2.ParseFromString(payload)
    assert(message.score == score)
    assert(message.num_players == num_players)
    assert(message.players == players)


def test_game_state():
    message = pb_server_game.GameState()
    playing = True
    seconds = 42
    winner = pb_server_game.RED
    message.playing = playing
    message.seconds = seconds
    message.winner = winner
    payload = message.SerializeToString()
    message2 = pb_server_game.GameState()
    message2.ParseFromString(payload)
    assert(message.playing == playing)
    assert(message.seconds == seconds)
    assert(message.winner == winner)


def test_welcome():
    message = pb_server_game.Welcome()
    robot = "TANK_1"
    team = pb_server_game.BLU
    playing = True
    seconds = 123456
    blu_score = 987
    blu_num = 3
    red_score = 654
    red_num = 2
    message.robot = robot
    message.team = team
    message.game_state.playing = playing
    message.game_state.seconds = seconds
    message.game_state.blu.score = blu_score
    message.game_state.blu.num_players = blu_num
    message.game_state.red.score = red_score
    message.game_state.red.num_players = red_num
    payload = message.SerializeToString()
    message2 = pb_server_game.Welcome()
    message2.ParseFromString(payload)
    assert(message2.robot == robot)
    assert(message2.team == team)
    assert(message2.game_state.playing == playing)
    assert(message2.game_state.seconds == seconds)
    assert(message2.game_state.blu.score == blu_score)
    assert(message2.game_state.blu.num_players == blu_num)
    assert(message2.game_state.red.score == red_score)
    assert(message2.game_state.red.num_players == red_num)


def test_access():
    message = pb_server_game.Access()
    port = 3
    ip = "1.2.3.4"
    message.port = port
    message.ip = ip
    payload = message.SerializeToString()
    message2 = pb_server_game.Access()
    message2.ParseFromString(payload)
    assert(message.port == port)
    assert(message.ip == ip)


def test_start():
    message = pb_server_game.Start()
    payload = message.SerializeToString()
    message2 = pb_server_game.Start()
    message2.ParseFromString(payload)


def test_stop():
    message = pb_server_game.Stop()
    shutdown = False
    video = True
    #message.shutdown = shutdown
    #message.video = video
    payload = message.SerializeToString()
    message2 = pb_server_game.Stop()
    message2.ParseFromString(payload)
    assert(message.shutdown == shutdown)
    assert(message.video == video)

# server-web


def test_get_access():
    message = pb_server_web.GetAccess()
    name = "TARTIFLETTE"
    message.name = name
    payload = message.SerializeToString()
    message2 = pb_server_web.GetAccess()
    message2.ParseFromString(payload)
    assert(message.name == name)


def test_get_game_state():
    message = pb_server_web.GetGameState()
    payload = message.SerializeToString()
    message2 = pb_server_web.GetGameState()
    message2.ParseFromString(payload)

# robot


def test_robot_state():
    message = pb_robot.RobotState()
    life = 120.42
    right = 2.25
    active = False
    message.life = life
    message.move.right = right
    message.active = active
    payload = message.SerializeToString()
    message2 = pb_robot.RobotState()
    message2.ParseFromString(payload)
    assert(message.life == life)
    assert(message.move.right == right)
    assert(message.active == active)


def test_video():
    message = pb_robot.Video()
    port = 42
    ip = "9.8.7.6"
    message.port = port
    message.ip = ip
    payload = message.SerializeToString()
    message2 = pb_robot.Video()
    message2.ParseFromString(payload)
    assert(message.port == port)
    assert(message.ip == ip)


# controller


def test_hello():
    message = pb_controller.Hello()
    name = "JAMBON"
    message.name = name
    payload = message.SerializeToString()
    message2 = pb_controller.Hello()
    message2.ParseFromString(payload)
    assert(message2.name == name)
    assert(message2.ready)


def test_input():
    message = pb_controller.Input()
    message.move.left = 0.2
    message.move.right = -0.5
    message.fire.weapon1 = False
    message.fire.weapon2 = True
    payload = message.SerializeToString()
    message2 = pb_controller.Input()
    message2.ParseFromString(payload)
    assert(message2.move.left == 0.2)
    assert(message2.move.right == -0.5)
    assert(not message2.fire.weapon1)
    assert(message2.fire.weapon2)


def main():
    old_test()
    # server-game
    test_team()
    test_game_state()
    test_welcome()
    test_access()
    test_start()
    test_stop()
    # server-web
    test_get_access()
    test_get_game_state()
    # robot
    test_robot_state()
    test_video()
    # controller
    test_hello()
    test_input()
    print "OK"

if ('__main__' == __name__):
    main()
