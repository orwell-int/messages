import orwell.messages.controller_pb2 as pb_controller
import orwell.messages.robot_pb2 as pb_robot
import orwell.messages.server_game_pb2 as pb_server_game
import orwell.messages.server_web_pb2 as pb_server_web


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
    assert(message2.score == score)
    assert(message2.num_players == num_players)
    assert(message2.players == players)


def test_game_state():
    message = pb_server_game.GameState()
    playing = True
    seconds = 42
    winner = "team_banana"
    message.playing = playing
    message.seconds = seconds
    message.winner = winner
    payload = message.SerializeToString()
    message2 = pb_server_game.GameState()
    message2.ParseFromString(payload)
    assert(message2.playing == playing)
    assert(message2.seconds == seconds)
    assert(message2.winner == winner)


def test_welcome(use_optional):
    message = pb_server_game.Welcome()
    robot = "TANK_1"
    team = "team_blue"
    robot_id = "84"
    playing = True
    seconds = 123456
    blu_score = 987
    blu_num = 3
    red_score = 654
    red_num = 2
    video_address = "127.0.0.2"
    video_port = 9009
    message.robot = robot
    message.team = team
    if (use_optional):
        message.game_state.playing = playing
        message.game_state.seconds = seconds
        team_blu = message.game_state.teams.add()
        team_blu.score = blu_score
        team_blu.num_players = blu_num
        team_red = message.game_state.teams.add()
        team_red.score = red_score
        team_red.num_players = red_num
    message.id = robot_id
    message.video_address = video_address
    message.video_port = video_port
    payload = message.SerializeToString()
    message2 = pb_server_game.Welcome()
    message2.ParseFromString(payload)
    assert(message2.robot == robot)
    assert(message2.team == team)
    if (use_optional):
        assert(message2.game_state.playing == playing)
        assert(message2.game_state.seconds == seconds)
        assert(message2.game_state.teams[0].score == blu_score)
        assert(message2.game_state.teams[0].num_players == blu_num)
        assert(message2.game_state.teams[1].score == red_score)
        assert(message2.game_state.teams[1].num_players == red_num)
    else:
        assert(not message2.game_state.playing)
        assert(message2.game_state.seconds == 0)
        assert(len(message2.game_state.teams) == 0)
    assert(message2.id == robot_id)
    assert(message.video_address == video_address)
    assert(message.video_port == video_port)


def test_access():
    message = pb_server_game.Access()
    port = 3
    ip = "1.2.3.4"
    message.port = port
    message.ip = ip
    payload = message.SerializeToString()
    message2 = pb_server_game.Access()
    message2.ParseFromString(payload)
    assert(message2.port == port)
    assert(message2.ip == ip)


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
    assert(message2.shutdown == shutdown)
    assert(message2.video == video)


def test_registered():
    message = pb_server_game.Registered()
    robot_id = 'Toto'
    team = "team_red"
    message.robot_id = robot_id
    message.team = team
    payload = message.SerializeToString()
    message2 = pb_server_game.Registered()
    message2.ParseFromString(payload)
    assert(message2.robot_id == robot_id)
    assert(message2.team == team)


# server-web


def test_get_access():
    message = pb_server_web.GetAccess()
    name = "TARTIFLETTE"
    message.name = name
    payload = message.SerializeToString()
    message2 = pb_server_web.GetAccess()
    message2.ParseFromString(payload)
    assert(message2.name == name)


def test_get_game_state():
    message = pb_server_web.GetGameState()
    payload = message.SerializeToString()
    message2 = pb_server_web.GetGameState()
    message2.ParseFromString(payload)

# robot


def test_server_robot_state():
    message = pb_robot.ServerRobotState()

    rfid_event1 = message.rfid.add()
    rfid_event2 = message.rfid.add()
    colour_event = message.colour.add()

    rfid_event1_timestamp = 1416757954
    rfid_event1_rfid = "myrfid"
    rfid_event1_status = pb_robot.ON
    rfid_event1.timestamp = rfid_event1_timestamp
    rfid_event1.rfid = rfid_event1_rfid
    rfid_event1.status = rfid_event1_status

    rfid_event2_timestamp = 1416757999
    rfid_event2_rfid = "myrfid"
    rfid_event2_status = pb_robot.OFF
    rfid_event2.timestamp = rfid_event2_timestamp
    rfid_event2.rfid = rfid_event2_rfid
    rfid_event2.status = rfid_event2_status

    colour_event_timestamp = 1416757955
    colour_event_colour = 5
    colour_event_status = pb_robot.ON
    colour_event.timestamp = colour_event_timestamp
    colour_event.colour = colour_event_colour
    colour_event.status = colour_event_status

    payload = message.SerializeToString()
    message2 = pb_robot.ServerRobotState()
    message2.ParseFromString(payload)

    assert(len(message2.rfid) == 2)
    assert(message2.rfid[0].timestamp == rfid_event1_timestamp)
    assert(message2.rfid[0].status == rfid_event1_status)
    assert(message2.rfid[0].rfid == rfid_event1_rfid)
    assert(message2.rfid[1].timestamp == rfid_event2_timestamp)
    assert(message2.rfid[1].status == rfid_event2_status)
    assert(message2.rfid[1].rfid == rfid_event2_rfid)
    assert(len(message2.colour) == 1)
    assert(message2.colour[0].timestamp == colour_event_timestamp)
    assert(message2.colour[0].status == colour_event_status)
    assert(message2.colour[0].colour == colour_event_colour)



def test_register():
    message = pb_robot.Register()
    temporary_robot_id = '192'
    video_url = "https://1.2.3.4:80/video"
    image = "image of my ball"
    message.temporary_robot_id = temporary_robot_id
    message.video_url = video_url
    message.image = image
    payload = message.SerializeToString()
    message2 = pb_robot.Register()
    message2.ParseFromString(payload)
    assert(message2.temporary_robot_id == temporary_robot_id)
    assert(message2.video_url == video_url)
    assert(message2.image == image)


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
    # server-game
    test_team()
    test_game_state()
    test_welcome(use_optional=True)
    test_welcome(use_optional=False)
    test_access()
    test_start()
    test_stop()
    test_registered()
    # server-web
    test_get_access()
    test_get_game_state()
    # robot
    test_server_robot_state()
    test_register()
    # controller
    test_hello()
    test_input()
    print "OK"

if ('__main__' == __name__):
    main()
